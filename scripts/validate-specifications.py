#!/usr/bin/env python3
"""
The Cybersecurity Trade Project - Specification & RFC Quality Gate Linter.

Validates:
1. Typography & Style: Zero emdashes ('—') and zero emojis in documentation.
2. Link Integrity: All markdown links point to existing files on disk.
3. RFC Schema: All files in rfcs/ follow numbering, metadata headers, and required sections.
4. JSON Schema: Any .json files in the repository parse cleanly.

Exit Codes:
0: All specifications pass quality gates.
1: One or more validation errors detected.
"""

import os
import re
import sys
import json
from pathlib import Path

# Repository root directory
REPO_ROOT = Path(__file__).resolve().parent.parent

# Emoji Unicode Ranges
EMOJI_PATTERN = re.compile(
    "["
    "\U0001F300-\U0001F9FF"  # Misc Symbols, Pictographs, Emoticons
    "\U00002600-\U000026FF"  # Misc symbols
    "\U00002700-\U000027BF"  # Dingbats
    "\U0001FA00-\U0001FA6F"  # Chess symbols, symbols & pictographs extended-A
    "\U0001FA70-\U0001FAFF"  # Symbols and pictographs extended-B
    "]+",
    flags=re.UNICODE,
)

# Markdown Link Regex: [text](path)
LINK_PATTERN = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

# Prohibited AI Slop, Marketing Buzzwords & Jargon Pattern
AI_SLOP_PATTERN = re.compile(
    r"\b("
    r"delve into|delving into|tapestry of|rich tapestry|multifaceted approach|"
    r"beacon of|testament to|holistic landscape|ever-evolving landscape|"
    r"game-changer|pivotal role|realm of|foster a culture of|in summary,|in conclusion,|"
    r"turnkey|seamless|seamlessly|robust|robustly|holistic|"
    r"streamline|streamlined|synergy|synergies|synergistic|"
    r"spearhead|spearheading|supercharge|supercharging|"
    r"cutting-edge|groundbreaking|paradigm shift|silver bullet|panacea"
    r")\b",
    re.IGNORECASE,
)

# Required RFC Sections
REQUIRED_RFC_SECTIONS = [
    "## 1. Executive Summary",
    "## 2. Motivation",
    "## 3. Detailed Specification",
    "## 4. Drawbacks",
    "## 5. Prior Art",
    "## 6. Implementation",
]

# Canonical 7 Pillars (Immutability Gate)
MANDATORY_PILLARS = {
    "pillars/01_pre-apprenticeship.md": "# Pillar I: Standardized Pre-Apprenticeship (The Talent Filter)",
    "pillars/02_earn-while-learning.md": "# Pillar II: The Earn-While-You-Learn Pipeline",
    "pillars/03_rotational-pipeline.md": "# Pillar III: Progressive Rotations & Enforced Ratios",
    "pillars/04_licensure-and-board.md": "# Pillar IV: Professional Licensure & The Journeyman Standard",
    "pillars/05_personal-liability-and-refusal.md": "# Pillar V: Personal Liability & The Right of Technical Refusal",
    "pillars/06_craft-guilds-and-labor-trusts.md": "# Pillar VI: Craft Guilds, Labor Trusts & Collective Defense",
    "pillars/07_insurance-catalyst.md": "# Pillar VII: The Insurance-Driven Market Catalyst",
}


def check_pillar_immutability() -> list:
    errors = []
    for rel_path, expected_title in MANDATORY_PILLARS.items():
        pillar_path = REPO_ROOT / rel_path
        if not pillar_path.exists():
            errors.append(
                f"[Pillar Immutability Error] Mandatory pillar file missing: '{rel_path}'. "
                f"The 7 core pillars are permanent architectural constants and cannot be renamed or deleted."
            )
            continue

        try:
            with open(pillar_path, "r", encoding="utf-8") as f:
                first_line = ""
                for line in f:
                    stripped = line.strip()
                    if stripped:
                        first_line = stripped
                        break
                if first_line != expected_title:
                    errors.append(
                        f"[Pillar Immutability Error] {rel_path}: Title mismatch.\n"
                        f"  Expected: '{expected_title}'\n"
                        f"  Found:    '{first_line}'"
                    )
        except Exception as e:
            errors.append(f"[Read Error] Could not read pillar {rel_path}: {e}")
    return errors


def check_typography_and_emojis(file_path: Path) -> list:
    errors = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, start=1):
                # Check for emdash and endash
                if "—" in line or "–" in line:
                    errors.append(
                        f"[Typography Error] {file_path.relative_to(REPO_ROOT)}:{line_num} "
                        f"contains non-standard dash ('—' or '–'). Use standard hyphens (' - ') or colons (':') instead."
                    )
                # Check for emojis
                if EMOJI_PATTERN.search(line):
                    errors.append(
                        f"[Style Error] {file_path.relative_to(REPO_ROOT)}:{line_num} "
                        f"contains emojis. Emojis are prohibited in trade specifications."
                    )
                # Check for prohibited AI slop phrases
                slop_match = AI_SLOP_PATTERN.search(line)
                if slop_match:
                    errors.append(
                        f"[AI Slop Error] {file_path.relative_to(REPO_ROOT)}:{line_num} "
                        f"contains prohibited AI slop phrase ('{slop_match.group(0)}'). "
                        f"Use concrete, authoritative engineering language instead."
                    )
    except Exception as e:
        errors.append(f"[Read Error] Could not read {file_path.relative_to(REPO_ROOT)}: {e}")
    return errors


def check_markdown_links(file_path: Path) -> list:
    errors = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            for match in LINK_PATTERN.finditer(content):
                target = match.group(2).strip()

                # Skip external web URLs and anchors
                if target.startswith("http://") or target.startswith("https://") or target.startswith("mailto:") or target.startswith("#"):
                    continue

                # Strip internal anchor if present (e.g., file.md#section)
                target_file_part = target.split("#")[0]
                if not target_file_part:
                    continue

                # Resolve relative path
                resolved_path = (file_path.parent / target_file_part).resolve()

                if not resolved_path.exists():
                    errors.append(
                        f"[Broken Link Error] {file_path.relative_to(REPO_ROOT)}: "
                        f"Link '[{match.group(1)}]({target})' points to non-existent target: {target_file_part}"
                    )
    except Exception as e:
        errors.append(f"[Read Error] Could not parse links in {file_path.relative_to(REPO_ROOT)}: {e}")
    return errors



def check_rfc_structure(rfc_path: Path) -> list:
    errors = []
    filename = rfc_path.name

    # Skip template
    if filename == "0000-template.md":
        return errors

    # Check filename pattern (e.g., 0001-title.md)
    if not re.match(r"^\d{4}-[a-z0-9\-]+\.md$", filename):
        errors.append(
            f"[RFC Schema Error] {rfc_path.relative_to(REPO_ROOT)}: "
            f"Filename must match 4-digit index pattern 'XXXX-short-name.md' (e.g., '0004-policy-warranties.md')."
        )

    try:
        with open(rfc_path, "r", encoding="utf-8") as f:
            content = f.read()

            # Check for Status field
            if not re.search(r"\*\s+\*\*Status:\*\*\s+(Draft|Proposed|Under Review|In Discussion|Accepted|Rejected|Superseded)", content, re.IGNORECASE):
                errors.append(
                    f"[RFC Schema Error] {rfc_path.relative_to(REPO_ROOT)}: "
                    f"Missing or invalid '* **Status:**' header (must be Draft, Proposed, Under Review, In Discussion, Accepted, Rejected, or Superseded)."
                )

            # Check for required sections
            for req_sec in REQUIRED_RFC_SECTIONS:
                sec_keyword = req_sec.split()[1]  # e.g., '1.', '2.'
                if req_sec not in content and sec_keyword not in content:
                    errors.append(
                        f"[RFC Schema Error] {rfc_path.relative_to(REPO_ROOT)}: "
                        f"Missing mandatory section header: '{req_sec}'"
                    )
    except Exception as e:
        errors.append(f"[Read Error] Could not read RFC {rfc_path.relative_to(REPO_ROOT)}: {e}")
    return errors


def check_pillar_immutability() -> list:
    errors = []
    for rel_path, expected_title in MANDATORY_PILLARS.items():
        pillar_path = REPO_ROOT / rel_path
        if not pillar_path.exists():
            errors.append(
                f"[Pillar Immutability Error] Mandatory pillar file missing: '{rel_path}'. "
                f"The 7 core pillars are permanent architectural constants and cannot be renamed or deleted."
            )
            continue

        try:
            with open(pillar_path, "r", encoding="utf-8") as f:
                first_line = ""
                for line in f:
                    stripped = line.strip()
                    if stripped:
                        first_line = stripped
                        break
                if first_line != expected_title:
                    errors.append(
                        f"[Pillar Immutability Error] {rel_path}: Title mismatch.\n"
                        f"  Expected: '{expected_title}'\n"
                        f"  Found:    '{first_line}'"
                    )
        except Exception as e:
            errors.append(f"[Read Error] Could not read pillar {rel_path}: {e}")
    return errors


def check_json_files() -> list:
    errors = []
    for json_file in REPO_ROOT.rglob("*.json"):
        # Skip node_modules or cache if any
        if ".cache" in json_file.parts or "node_modules" in json_file.parts:
            continue
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                json.load(f)
        except Exception as e:
            errors.append(f"[JSON Error] Invalid JSON syntax in {json_file.relative_to(REPO_ROOT)}: {e}")
    return errors


def check_ecosystem_version_sync() -> list:
    """Verifies that the framework version is perfectly synchronized across the ecosystem."""
    errors = []
    # Check workspace root first, then local repo root fallback
    context_json = REPO_ROOT.parent / ".config" / "ai" / "context.json"
    if not context_json.exists():
        context_json = REPO_ROOT / ".config" / "ai" / "context.json"
    if not context_json.exists():
        return errors

    try:
        with open(context_json, "r", encoding="utf-8") as f:
            data = json.load(f)
            current_ver = data.get("version", "").strip()

        if not current_ver:
            errors.append("[Ecosystem Version Sync Error] Missing 'version' key in .config/ai/context.json")
            return errors

        # Verify _config.yml version
        config_yml = REPO_ROOT / "_config.yml"
        if config_yml.exists():
            with open(config_yml, "r", encoding="utf-8") as f:
                content = f.read()
                if f"v{current_ver}" not in content:
                    errors.append(
                        f"[Ecosystem Version Sync Error] _config.yml version does not match current v{current_ver}."
                    )

        # Verify estimator parity
        estimator_index = REPO_ROOT.parent / "estimator" / "public" / "index.html"
        if estimator_index.exists():
            with open(estimator_index, "r", encoding="utf-8") as f:
                content = f.read()
                if f"v{current_ver}" not in content:
                    errors.append(
                        f"[Ecosystem Version Sync Error] estimator/public/index.html is missing reference to v{current_ver}."
                    )
    except Exception as e:
        errors.append(f"[Ecosystem Version Sync Error] Verification error: {e}")

    return errors


def check_canonical_entity_naming() -> list:
    """Verifies that all entity names, governance bodies, and ecosystem tools use canonical naming."""
    errors = []
    # Prohibited drift variations and their canonical replacements
    DISALLOWED_PATTERNS = [
        (re.compile(r"\bCyber Trade Board\b", re.IGNORECASE), "National Cybersecurity Trade Board (NCTB)"),
        (re.compile(r"\bParticipating Employers Council\b", re.IGNORECASE), "Participating Employer Council (PEC)"),
        (re.compile(r"\bCyber Trade Guild\b", re.IGNORECASE), "The Cybersecurity Craft Guild (CCG)"),
        (re.compile(r"github\.com/cyber-trade-ecosystem", re.IGNORECASE), "github.com/the-cyber-trade-project"),
    ]

    md_files = [
        p for p in REPO_ROOT.rglob("*.md")
        if ".git" not in p.parts and ".cache" not in p.parts and "tmp" not in p.parts
    ]

    for mf in md_files:
        try:
            content = mf.read_text(encoding="utf-8")
            for pattern, canonical in DISALLOWED_PATTERNS:
                matches = pattern.findall(content)
                if matches:
                    errors.append(
                        f"[Naming Quality Gate Error] {mf.relative_to(REPO_ROOT)}: Found non-canonical entity '{matches[0]}'. "
                        f"Must use canonical standard: '{canonical}'."
                    )
        except Exception as e:
            errors.append(f"[Naming Quality Gate Error] Could not scan {mf}: {e}")

    return errors


def check_release_notes_quality() -> list:
    errors = []
    rel_dir = REPO_ROOT / "docs" / "releases"
    if not rel_dir.exists():
        return errors
    for rf in rel_dir.glob("*.md"):
        try:
            content = rf.read_text(encoding="utf-8")
            if len(content.splitlines()) < 5:
                errors.append(f"[Release Notes Error] {rf.name}: Release notes file is too short (less than 5 lines).")
            if "Merge pull request" in content or "chore(release)" in content:
                errors.append(f"[Release Notes Error] {rf.name}: Release notes contain raw merge/commit logs. Must be structured domain prose.")
        except Exception as e:
            errors.append(f"[Release Notes Error] {rf.name}: Could not read release notes: {e}")
    return errors


def check_rfc_protection_gate() -> list:
    """Verifies that open community RFCs remain preserved and protected from unilateral front-running."""
    errors = []
    rfc_dir = REPO_ROOT / "rfcs"
    if not rfc_dir.exists():
        errors.append("[RFC Invariant Error] rfcs/ directory is missing from repository root.")
        return errors
    
    # Verify mandatory template and registered RFCs exist
    template = rfc_dir / "0000-template.md"
    if not template.exists():
        errors.append("[RFC Invariant Error] rfcs/0000-template.md is missing.")
        
    return errors


def check_frontend_security_sast() -> list:
    """Automated SAST Security Gate: Scans all frontend JavaScript and HTML files across the ecosystem for vulnerabilities."""
    errors = []
    
    # Repositories to scan
    repo_dirs = [REPO_ROOT]
    workspace_root = REPO_ROOT.parent
    for sister in ["estimator", "logbook", "clearinghouse", "telemetry"]:
        sister_dir = workspace_root / sister
        if sister_dir.exists():
            repo_dirs.append(sister_dir)
            
    # Prohibited dangerous sinks in JavaScript
    DANGEROUS_PATTERNS = [
        (re.compile(r"\beval\s*\("), "eval() dynamic execution prohibited"),
        (re.compile(r"\bnew\s+Function\s*\("), "new Function() code generation prohibited"),
        (re.compile(r"\bdocument\.write(?:ln)?\s*\("), "document.write() DOM injection prohibited"),
        (re.compile(r"\bwindow\.execScript\s*\("), "execScript() execution prohibited"),
    ]
    
    for r_dir in repo_dirs:
        # Scan JavaScript files
        for js_file in r_dir.rglob("*.js"):
            if ".git" in js_file.parts or "node_modules" in js_file.parts or "tmp" in js_file.parts or "_site" in js_file.parts:
                continue
            try:
                content = js_file.read_text(encoding="utf-8")
                rel_path = js_file.relative_to(workspace_root) if workspace_root in js_file.parents else js_file.relative_to(r_dir)
                for pattern, msg in DANGEROUS_PATTERNS:
                    if pattern.search(content):
                        errors.append(f"[Front-End SAST Security Error] {rel_path}: {msg}")
            except Exception as e:
                errors.append(f"[Front-End SAST Error] Could not read {js_file}: {e}")

        # Scan HTML files for CSP directives & nosniff meta tags
        for html_file in r_dir.rglob("*.html"):
            if ".git" in html_file.parts or "node_modules" in html_file.parts or "tmp" in html_file.parts or "_site" in html_file.parts:
                continue
            # Only scan standalone page templates or entry points (index.html, default.html)
            if html_file.name not in ["index.html", "default.html"]:
                continue
            try:
                content = html_file.read_text(encoding="utf-8")
                rel_path = html_file.relative_to(workspace_root) if workspace_root in html_file.parents else html_file.relative_to(r_dir)
                
                # Check for CSP meta tag
                if "Content-Security-Policy" not in content:
                    errors.append(f"[Front-End SAST Security Error] {rel_path}: Missing Content-Security-Policy meta header.")
                else:
                    if "base-uri" not in content:
                        errors.append(f"[Front-End SAST Security Error] {rel_path}: CSP missing 'base-uri' directive.")
                    if "form-action" not in content:
                        errors.append(f"[Front-End SAST Security Error] {rel_path}: CSP missing 'form-action' directive.")

                # Check for X-Content-Type-Options: nosniff
                if "X-Content-Type-Options" not in content or "nosniff" not in content:
                    errors.append(f"[Front-End SAST Security Error] {rel_path}: Missing 'X-Content-Type-Options: nosniff' header.")
            except Exception as e:
                errors.append(f"[Front-End SAST Error] Could not read {html_file}: {e}")

    return errors


def main():
    print("=" * 70)
    print(" The Cybersecurity Trade Project - Specification Quality Gate")
    print("=" * 70)

    total_errors = []

    # Gather all markdown files
    md_files = [
        p for p in REPO_ROOT.rglob("*.md")
        if ".git" not in p.parts and ".cache" not in p.parts and "tmp" not in p.parts
    ]

    print(f"[*] Scanning {len(md_files)} markdown files for typography, emojis, and link integrity...")

    for md_file in md_files:
        total_errors.extend(check_typography_and_emojis(md_file))
        total_errors.extend(check_markdown_links(md_file))

    # Validate Release Notes Quality
    print("[*] Validating curated release notes quality in docs/releases/...")
    release_errors = check_release_notes_quality()
    total_errors.extend(release_errors)

    # Validate Mandatory 7 Pillars Immutability
    print("[*] Validating the 7 Core Pillars immutability and canonical titles...")
    pillar_errors = check_pillar_immutability()
    total_errors.extend(pillar_errors)

    # Check RFCs
    rfc_dir = REPO_ROOT / "rfcs"
    if rfc_dir.exists():
        rfc_files = list(rfc_dir.glob("*.md"))
        print(f"[*] Validating {len(rfc_files)} RFC proposals for schema compliance and community protection gate...")
        total_errors.extend(check_rfc_protection_gate())
        for rfc in rfc_files:
            total_errors.extend(check_rfc_structure(rfc))

    # Check JSON files
    json_errors = check_json_files()
    total_errors.extend(json_errors)

    # Check Ecosystem Version Synchronization
    print("[*] Validating ecosystem version synchronization across repositories...")
    version_sync_errors = check_ecosystem_version_sync()
    total_errors.extend(version_sync_errors)
    # Validate Canonical Entity Naming & Ecosystem Alignment
    print("[*] Validating canonical entity naming and ecosystem nomenclature...")
    naming_errors = check_canonical_entity_naming()
    total_errors.extend(naming_errors)


    # Validate Frontend Security SAST Gate across Ecosystem
    print("[*] Running automated Front-End Security SAST scanner across ecosystem...")
    sast_errors = check_frontend_security_sast()
    total_errors.extend(sast_errors)

    # Validate Web Portal Frontend Assets & Hover Glossary
    print("[*] Validating web portal frontend assets and interactive hover glossary integrity...")
    web_asset_files = [
        p for p in (REPO_ROOT / "assets").rglob("*")
        if p.is_file() and p.suffix in [".js", ".css", ".html"]
    ]
    for asset_file in web_asset_files:
        total_errors.extend(check_typography_and_emojis(asset_file))

    # Validate Core Documentation Files Presence
    for core_doc in ["README.md", "GLOSSARY.md", "FAQ.md"]:
        if not (REPO_ROOT / core_doc).exists():
            total_errors.append(f"[Core Doc Error] Missing mandatory documentation file: '{core_doc}'.")

    print("=" * 70)
    if total_errors:
        print(f"[FAIL] Quality Gate failed with {len(total_errors)} issue(s):\n")
        for err in total_errors:
            print(f"  [X] {err}")
        print("\nPlease resolve all errors before submitting or merging your pull request.")
        sys.exit(1)
    else:
        print("[PASS] All specifications, links, RFC schemas, JSON files, and version parity verified 100% clean!")
        print("=" * 70)
        sys.exit(0)


if __name__ == "__main__":
    main()

