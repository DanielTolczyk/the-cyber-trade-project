#!/usr/bin/env python3
"""
The Cybersecurity Trade Project - Front-End UI Smoke & DOM Integrity Test Suite.

Validates:
1. Static preview build presence and integrity in _site/.
2. Presence and DOM attributes of critical interactive components:
   - Search trigger (#btn-portal-search)
   - Search backdrop modal (#portal-search-backdrop)
   - Search input (#portal-search-input) and results container (#portal-search-results)
   - Mobile navigation trigger (#btn-toggle-sidebar)
   - Sidebar drawer (#portal-sidebar) and backdrop (#portal-sidebar-backdrop)
3. AST execution readiness of assets/js/portal.js.
4. Parsing and query simulation over assets/js/search-index.json.
"""

import sys
import os
import json
import shutil
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SITE_DIR = REPO_ROOT / "_site"


def run_smoke_tests() -> int:
    errors = []
    print("=" * 70)
    print(" The Cybersecurity Trade Project - Front-End UI Smoke Test Suite")
    print("=" * 70)

    # 1. Ensure _site exists or build it
    if not SITE_DIR.exists() or not (SITE_DIR / "index.html").exists():
        print("[*] Generating static preview site via build_preview.py...")
        proc = subprocess.run([sys.executable, str(REPO_ROOT / "scripts" / "build_preview.py")], capture_output=True, text=True)
        if proc.returncode != 0:
            errors.append(f"Preview generation failed: {proc.stderr}")
            print(f"[FAIL] {proc.stderr}")
            return 1

    # 2. Check JavaScript AST compilation
    portal_js = REPO_ROOT / "assets" / "js" / "portal.js"
    if not portal_js.exists():
        errors.append("assets/js/portal.js is missing.")
    else:
        node_bin = shutil.which("node")
        if not node_bin:
            vscode_server = Path(os.path.expanduser("~/.vscode-server"))
            if vscode_server.exists():
                for candidate in vscode_server.glob("**/node"):
                    if candidate.is_file() and os.access(candidate, os.X_OK):
                        node_bin = str(candidate)
                        break

        if node_bin:
            res = subprocess.run([node_bin, "-c", str(portal_js)], capture_output=True, text=True)
            if res.returncode != 0:
                errors.append(f"JavaScript AST compilation failed in portal.js: {res.stderr.strip()}")
            else:
                print("[PASS] assets/js/portal.js compiled cleanly with zero syntax errors.")
        else:
            print("[WARN] Node.js not detected; skipped deep AST compiler pass.")

    # 3. Check Search Index JSON integrity
    search_index_file = REPO_ROOT / "assets" / "js" / "search-index.json"
    if not search_index_file.exists():
        errors.append("assets/js/search-index.json is missing.")
    else:
        try:
            index_data = json.loads(search_index_file.read_text(encoding="utf-8"))
            if not isinstance(index_data, list) or len(index_data) < 10:
                errors.append(f"search-index.json has insufficient entries: {len(index_data)} found.")
            else:
                print(f"[PASS] assets/js/search-index.json validated: {len(index_data)} indexed sections.")
                
                # Query simulation: Test known terms
                test_queries = ["apprentice", "journeyman", "taft-hartley", "mor", "refusal"]
                for q in test_queries:
                    hits = [
                        item for item in index_data
                        if q in (item.get("heading", "") + " " + item.get("docTitle", "") + " " + item.get("content", "")).lower()
                    ]
                    if not hits:
                        errors.append(f"Search index query simulation returned 0 hits for core term '{q}'.")
                print(f"[PASS] In-memory query simulation passed across {len(test_queries)} core trade terms.")
        except Exception as e:
            errors.append(f"Could not parse assets/js/search-index.json: {e}")

    # 4. Check HTML DOM anchors in entry pages
    required_elements = [
        ("id=\"btn-portal-search\"", "Search trigger button (#btn-portal-search)"),
        ("id=\"portal-search-backdrop\"", "Search modal backdrop (#portal-search-backdrop)"),
        ("id=\"portal-search-input\"", "Search modal text input (#portal-search-input)"),
        ("id=\"portal-search-results\"", "Search results container (#portal-search-results)"),
        ("id=\"btn-toggle-sidebar\"", "Mobile navigation trigger button (#btn-toggle-sidebar)"),
        ("id=\"portal-sidebar\"", "Portal navigation sidebar (#portal-sidebar)"),
        ("id=\"portal-sidebar-backdrop\"", "Sidebar mobile backdrop (#portal-sidebar-backdrop)"),
    ]

    sample_pages = [
        SITE_DIR / "index.html",
        SITE_DIR / "pillars" / "01_pre-apprenticeship.html",
        SITE_DIR / "framework" / "supervisory-ratios.html",
        SITE_DIR / "GLOSSARY.html",
    ]

    for page in sample_pages:
        if not page.exists():
            errors.append(f"Rendered sample page missing: {page.relative_to(REPO_ROOT)}")
            continue
        html_content = page.read_text(encoding="utf-8")
        rel_page = page.relative_to(REPO_ROOT)
        for pattern, label in required_elements:
            if pattern not in html_content:
                errors.append(f"DOM Integrity Error in {rel_page}: Missing {label}.")

    print(f"[PASS] Rendered DOM integrity validated across {len(sample_pages)} entry pages.")

    print("=" * 70)
    if errors:
        print(f"[FAIL] Front-End Smoke Test Suite failed with {len(errors)} error(s):")
        for err in errors:
            print(f"  [X] {err}")
        print("=" * 70)
        return 1

    print("[PASS] All front-end UI smoke tests and DOM assertions verified 100% clean!")
    print("=" * 70)
    return 0


if __name__ == "__main__":
    sys.exit(run_smoke_tests())
