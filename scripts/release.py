#!/usr/bin/env python3
"""
The Cybersecurity Trade Project - Automated Release Engine.
Handles: Quality gate, SemVer calculation, PR flow, tagging, and GitHub Releases.
"""

import os
import sys
import re
import json
import time
import argparse
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
VALIDATE_SCRIPT = REPO_ROOT / "scripts" / "validate-specifications.py"


def run_cmd(cmd, check=True):
    res = subprocess.run(
        cmd,
        cwd=REPO_ROOT,
        shell=isinstance(cmd, str),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if check and res.returncode != 0:
        err = res.stderr.strip() if res.stderr else "Unknown error"
        raise RuntimeError(f"Command failed [{cmd}]: {err}")
    return res.stdout.strip() if res.stdout else ""


def validate_specifications():
    print("[*] Running pre-flight specification quality gate...")
    if not VALIDATE_SCRIPT.exists():
        raise FileNotFoundError(f"Validator missing at {VALIDATE_SCRIPT}")
    res = subprocess.run([sys.executable, str(VALIDATE_SCRIPT)], cwd=REPO_ROOT)
    if res.returncode != 0:
        raise RuntimeError("Specification quality gate failed. Aborting release.")
    print("[PASS] Quality gate clean (0 emdashes, 0 emojis, 100% link integrity).")


def get_latest_tag() -> str:
    try:
        tags = run_cmd("git tag -l 'v*'").splitlines()
        if tags:
            def parse_tag(t):
                m = re.match(r"^v?(\d+)\.(\d+)\.(\d+)", t)
                return tuple(map(int, m.groups())) if m else (0, 0, 0)
            return sorted(tags, key=parse_tag)[-1]
    except Exception:
        pass
    return "v1.0.0"


def calculate_next_version(current_tag: str, bump_type: str) -> str:
    m = re.match(r"^v?(\d+)\.(\d+)\.(\d+)", current_tag)
    if not m:
        raise ValueError(f"Tag '{current_tag}' is not valid SemVer.")
    maj, min_, pat = map(int, m.groups())
    if bump_type == "major":
        return f"v{maj + 1}.0.0"
    elif bump_type == "minor":
        return f"v{maj}.{min_ + 1}.0"
    return f"v{maj}.{min_}.{pat + 1}"


def handle_open_prs(include_pr_ids=None, dry_run=False) -> list:
    """Inspects open PRs, preserves RFCs, and prompts on non-RFC PRs."""
    print("[*] Inspecting active PRs and open RFC branches...")
    merged_prs = []
    try:
        prs_json = run_cmd("gh pr list --json number,title,headRefName,isDraft", check=False)
        if not prs_json:
            return merged_prs
        
        prs = json.loads(prs_json)
        rfc_prs = []
        non_rfc_prs = []
        
        for p in prs:
            head = p.get("headRefName", "")
            title = p.get("title", "")
            if head.startswith("rfc/") or title.startswith("RFC"):
                rfc_prs.append(p)
            else:
                non_rfc_prs.append(p)
        
        if rfc_prs:
            print(f"[*] Preserving {len(rfc_prs)} active RFC branches for community review:")
            for rfc in rfc_prs:
                print(f"    - #{rfc['number']}: {rfc['title']} ({rfc['headRefName']})")
        
        if non_rfc_prs:
            print(f"[*] Found {len(non_rfc_prs)} open non-RFC PR(s):")
            for pr in non_rfc_prs:
                pr_num = pr["number"]
                pr_title = pr["title"]
                pr_branch = pr["headRefName"]
                
                should_include = False
                if include_pr_ids and pr_num in include_pr_ids:
                    should_include = True
                elif sys.stdin.isatty() and not dry_run:
                    try:
                        ans = input(f"[?] Include PR #{pr_num}: '{pr_title}' ({pr_branch}) in this release? [y/N]: ").strip().lower()
                        should_include = (ans == "y" or ans == "yes")
                    except EOFError:
                        should_include = False
                
                if should_include:
                    if dry_run:
                        print(f"    [DRY RUN] Would merge PR #{pr_num}: {pr_title}")
                    else:
                        print(f"[*] Merging PR #{pr_num}: {pr_title}...")
                        run_cmd(f"gh pr merge {pr_num} --merge --delete-branch")
                        merged_prs.append(pr)
                        print(f"[+] PR #{pr_num} merged.")
                else:
                    print(f"    [-] Preserving PR #{pr_num} (left open).")
    except Exception as e:
        print(f"[-] Note: Could not query GitHub PR list ({e}).")
    return merged_prs



def generate_notes(version: str, title: str, prev_tag: str) -> str:
    """Reads curated release notes from docs/releases/<version>.md."""
    v_clean = version if version.startswith("v") else f"v{version}"
    rel_notes_file = REPO_ROOT / "docs" / "releases" / f"{v_clean}.md"
    if not rel_notes_file.exists():
        rel_notes_file = REPO_ROOT / "docs" / "releases" / f"{v_clean.lstrip('v')}.md"
    
    if rel_notes_file.exists():
        content = rel_notes_file.read_text(encoding="utf-8").strip()
    else:
        raise FileNotFoundError(
            f"Mandatory release notes file missing: 'docs/releases/{v_clean}.md'. "
            f"Please author comprehensive, structured release notes before publishing."
        )

    changelog_link = f"**Full Changelog**: https://github.com/DanielTolczyk/the-cyber-trade-project/compare/{prev_tag}...{v_clean}"
    return f"{content}\n\n{changelog_link}"


def get_semantic_commit_type(bump_type: str, title: str) -> str:
    if bump_type in ["minor", "major"]:
        return "feat"
    lower = title.lower()
    if any(w in lower for w in ["fix", "security", "harden", "patch", "repair", "csrf", "xss"]):
        return "fix"
    return "docs"



def sync_ecosystem_metadata(target_version: str):
    """Synchronizes version metadata across _config.yml, context.json, and sister repositories."""
    raw_ver = target_version.lstrip("v")
    v_str = f"v{raw_ver}"

    # 1. Update _config.yml
    config_path = REPO_ROOT / "_config.yml"
    if config_path.exists():
        with open(config_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        with open(config_path, "w", encoding="utf-8") as f:
            for line in lines:
                if line.startswith("version:"):
                    f.write(f'version: "{v_str}"\n')
                else:
                    f.write(line)

    # 2. Update .config/ai/context.json
    context_path = REPO_ROOT / ".config" / "ai" / "context.json"
    if context_path.exists():
        with open(context_path, "r", encoding="utf-8") as f:
            cdata = json.load(f)
        cdata["version"] = raw_ver
        cdata["last_updated"] = time.strftime("%Y-%m-%d %H:%M")
        with open(context_path, "w", encoding="utf-8") as f:
            json.dump(cdata, f, indent=2)

    # 3. Update Estimator footer
    estimator_index = REPO_ROOT.parent / "cyber-trade-estimator" / "public" / "index.html"
    if estimator_index.exists():
        with open(estimator_index, "r", encoding="utf-8") as f:
            text = f.read()
        text = re.sub(r"The Cybersecurity Trade Project \(v[0-9.]+\)", f"The Cybersecurity Trade Project ({v_str})", text)
        with open(estimator_index, "w", encoding="utf-8") as f:
            f.write(text)

    # 4. Update Logbook specifications framework_version
    logbook_specs = REPO_ROOT.parent / "cyber-trade-logbook" / "public" / "data" / "logbook_specifications.json"
    if logbook_specs.exists():
        with open(logbook_specs, "r", encoding="utf-8") as f:
            ldata = json.load(f)
        ldata["framework_version"] = raw_ver
        with open(logbook_specs, "w", encoding="utf-8") as f:
            json.dump(ldata, f, indent=2)


def execute_release(args):
    prev_tag = get_latest_tag()
    target_version = args.version if args.version else calculate_next_version(prev_tag, args.type)
    if not target_version.startswith("v"):
        target_version = f"v{target_version}"

    # Synchronize metadata before pre-flight validation
    sync_ecosystem_metadata(target_version)
    validate_specifications()
    
    release_title = args.title or f"Specification and Governance Update ({target_version})"
    release_title = release_title.replace("—", "-")
    
    print(f"\n[*] Release Target: {prev_tag} -> {target_version}")
    print(f"[*] Release Title:  {release_title}")
    
    include_prs = [int(p) for p in args.include_pr] if args.include_pr else None
    merged_prs = handle_open_prs(include_pr_ids=include_prs, dry_run=args.dry_run)

    status = run_cmd("git status --porcelain")
    has_pending = bool(status.strip())
    branch_name = f"release/{target_version}"

    if args.dry_run:
        print("\n[DRY RUN] Release workflow validated successfully.")
        print(f"  Branch:       {branch_name}")
        print(f"  Version:      {target_version}")
        print(f"  Pending:      {'Yes' if has_pending else 'No'}")
        print(f"  Merged PRs:   {len(merged_prs)}")
        print("\n[DRY RUN] Generated Release Notes:\n" + generate_notes(target_version, release_title, prev_tag))
        return

    if has_pending:
        current_branch = run_cmd("git branch --show-current")
        if current_branch != branch_name:
            branches = [b.strip("* ") for b in run_cmd("git branch --list").splitlines()]
            if branch_name in branches:
                print(f"[*] Switching to existing release branch '{branch_name}'...")
                run_cmd(f"git checkout {branch_name}")
            else:
                print(f"[*] Creating release branch '{branch_name}'...")
                run_cmd(f"git checkout -b {branch_name}")
        else:
            print(f"[*] Already on release branch '{branch_name}'.")
        sem_type = get_semantic_commit_type(args.type, release_title)
        print("[*] Staging and committing changes...")
        run_cmd("git add -A")
        run_cmd(["git", "commit", "-m", f"{sem_type}(release): prepare {target_version} - {release_title}"])
        print(f"[*] Pushing '{branch_name}' to origin...")
        run_cmd(f"git push -u origin {branch_name}")

        notes = generate_notes(target_version, release_title, prev_tag)
        print("[*] Creating Pull Request...")
        pr_cmd = ["gh", "pr", "create", "--base", "main", "--head", branch_name, "--title", f"{sem_type}(release): {target_version} - {release_title}", "--body", notes]
        run_cmd(pr_cmd)

        print("[*] Merging Pull Request into main...")
        run_cmd("gh pr merge --merge --delete-branch")

    print("[*] Updating local main branch...")
    run_cmd("git checkout main")
    run_cmd("git pull origin main")

    print(f"[*] Tagging release '{target_version}'...")
    run_cmd(["git", "tag", "-fa", target_version, "-m", f"Release {target_version}: {release_title}"])
    run_cmd(f"git push origin {target_version} --force")

    notes = generate_notes(target_version, release_title, prev_tag)
    print(f"[*] Creating GitHub Release '{target_version}'...")
    run_cmd(["gh", "release", "create", target_version, "--title", f"{target_version}: {release_title}", "--notes", notes])
    print(f"\n[SUCCESS] Release {target_version} successfully published on GitHub!")


def main():
    parser = argparse.ArgumentParser(description="The Cybersecurity Trade Project - Automated Release Engine")
    parser.add_argument("type", nargs="?", choices=["patch", "minor", "major"], default="patch")
    parser.add_argument("--version", "-v", help="Explicit version (e.g. v1.7.0)")
    parser.add_argument("--title", "-t", help="Release title summary")
    parser.add_argument("--include-pr", "-p", nargs="+", help="Specific open PR numbers to merge into this release")
    parser.add_argument("--dry-run", action="store_true", help="Simulate without modifying remote state")
    args = parser.parse_args()
    try:
        execute_release(args)
    except Exception as e:
        print(f"\n[ERROR] Release failed: {e}", file=sys.stderr)
        sys.exit(1)



if __name__ == "__main__":
    main()

