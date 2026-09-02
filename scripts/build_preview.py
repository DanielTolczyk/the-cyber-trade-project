#!/usr/bin/env python3
"""
The Cybersecurity Trade Project - Local Preview Site Generator.
Builds a static HTML preview in _site/ mirroring GitHub Pages Jekyll layout.
"""

import os
import re
import shutil
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SITE_DIR = REPO_ROOT / "_site"


def generate_search_index(md_files):
    """Generates a secure, pre-compiled JSON search index of all specifications."""
    index = []
    category_map = {
        "pillars": "The 7 Core Pillars",
        "framework": "Operational Framework",
        "governance": "Governance & Legal",
        "docs": "Primers & Guides",
        "templates": "Procedural Forms",
    }
    
    for md_path in md_files:
        if "rfcs" in md_path.parts or ".github" in md_path.parts or "tmp" in md_path.parts or "scripts" in md_path.parts:
            continue
        rel = md_path.relative_to(REPO_ROOT)
        dest_rel = rel.with_suffix(".html")
        if rel.name == "README.md":
            dest_rel = rel.parent / "index.html"
            
        url = "/" + str(dest_rel).replace("\\", "/")
        if url.endswith("/index.html"):
            url = url[:-10] or "/"
            
        parent_dir = rel.parts[0] if len(rel.parts) > 1 else "root"
        category = category_map.get(parent_dir, "General Specification")
        
        md_text = md_path.read_text(encoding="utf-8")
        lines = md_text.splitlines()
        
        # Extract title
        title = ""
        for line in lines:
            line_s = line.strip()
            if line_s.startswith("# "):
                title = line_s[2:].strip()
                break
            elif line_s.startswith("title: "):
                title = line_s[7:].strip().strip('"').strip("'")
                
        if not title:
            title = rel.stem.replace("-", " ").replace("_", " ").title()
            
        # Extract headings
        headings = []
        for line in lines:
            line_s = line.strip()
            if line_s.startswith("## ") or line_s.startswith("### "):
                h_text = re.sub(r"^#+\s*", "", line_s).strip()
                headings.append(h_text)
                
        # Extract content snippet
        clean_lines = []
        for line in lines:
            line_s = line.strip()
            if not line_s.startswith("#") and not line_s.startswith("---") and not line_s.startswith("```"):
                clean_lines.append(re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line_s))
                
        snippet = " ".join(clean_lines)[:350]
        
        index.append({
            "title": title,
            "url": url,
            "category": category,
            "headings": headings[:15],
            "snippet": snippet
        })
        
    index_path = REPO_ROOT / "assets" / "js" / "search-index.json"
    index_path.parent.mkdir(parents=True, exist_ok=True)
    index_path.write_text(json.dumps(index, indent=2), encoding="utf-8")
    
    site_index = SITE_DIR / "assets" / "js" / "search-index.json"
    site_index.parent.mkdir(parents=True, exist_ok=True)
    site_index.write_text(json.dumps(index, indent=2), encoding="utf-8")


def parse_tables(lines: list) -> list:
    """Converts Markdown table syntax to HTML tables."""
    output = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        # Check for table header followed by separator (|:---|:---|)
        if line.startswith("|") and i + 1 < len(lines) and re.match(r"^\|?[\s:\-]+\|[\s:\-|]+$", lines[i+1].strip()):
            headers = [c.strip() for c in line.split("|")[1:-1]] if line.endswith("|") else [c.strip() for c in line.split("|")[1:]]
            output.append("<table>")
            output.append("<thead><tr>")
            for h in headers:
                output.append(f"<th>{h}</th>")
            output.append("</tr></thead>")
            output.append("<tbody>")
            
            i += 2  # Skip header and separator
            while i < len(lines) and lines[i].strip().startswith("|"):
                row = lines[i].strip()
                cells = [c.strip() for c in row.split("|")[1:-1]] if row.endswith("|") else [c.strip() for c in row.split("|")[1:]]
                output.append("<tr>")
                for c in cells:
                    output.append(f"<td>{c}</td>")
                output.append("</tr>")
                i += 1
            output.append("</tbody></table>")
        else:
            output.append(lines[i])
            i += 1
    return output


def md_to_html(md_text: str) -> str:
    """Markdown to HTML converter with code block preservation, tables, and nested lists."""
    # 1. Extract and preserve code blocks
    code_blocks = {}
    
    def extract_code_block(m):
        idx = len(code_blocks)
        placeholder = f"___CODE_BLOCK_{idx}___"
        code = m.group(1)
        code_escaped = code.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        code_blocks[placeholder] = f"<pre><code>{code_escaped}</code></pre>"
        return placeholder
    
    html = re.sub(r"```(?:\w+)?\n(.*?)```", extract_code_block, md_text, flags=re.DOTALL)
    
    # 2. Inline code
    html = re.sub(r"`([^`]+)`", r"<code>\1</code>", html)
    
    # 3. Headings
    html = re.sub(r"^### (.*?)$", r"<h3>\1</h3>", html, flags=re.MULTILINE)
    html = re.sub(r"^## (.*?)$", r"<h2>\1</h2>", html, flags=re.MULTILINE)
    html = re.sub(r"^# (.*?)$", r"<h1>\1</h1>", html, flags=re.MULTILINE)
    
    # 4. Blockquotes
    html = re.sub(r"^> (.*?)$", r"<blockquote><p>\1</p></blockquote>", html, flags=re.MULTILINE)
    
    # 5. Horizontal rules
    html = re.sub(r"^---+$", r"<hr>", html, flags=re.MULTILINE)
    
    # 6. Images & Links
    html = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", r'<img src="\2" alt="\1">', html)
    
    def replace_links(m):
        text = m.group(1)
        url = m.group(2)
        if url.endswith(".md"):
            url = url[:-3] + ".html"
        return f'<a href="{url}">{text}</a>'
    
    html = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", replace_links, html)
    
    # 7. Bold (Process before italics, ignore single bullet asterisks)
    html = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", html)
    
    # 8. Tables and Nested Lists
    lines = parse_tables(html.splitlines())
    output_lines = []
    list_stack = []  # Tracks nesting levels [indent_level]

    for line in lines:
        stripped = line.strip()
        
        # Check if line is a bullet item
        match_bullet = re.match(r"^(\s*)[*\-]\s+(.*)$", line)
        
        if stripped.startswith("___CODE_BLOCK_"):
            while list_stack:
                output_lines.append("</ul>")
                list_stack.pop()
            output_lines.append(stripped)
            continue
            
        if match_bullet:
            indent_len = len(match_bullet.group(1))
            content = match_bullet.group(2)
            
            # Apply italics within list item content only if not bold
            content = re.sub(r"(?<!\*)_([^_]+)_(?!\*)", r"<em>\1</em>", content)
            
            if not list_stack:
                output_lines.append('<ul class="portal-list">')
                list_stack.append(indent_len)
            elif indent_len > list_stack[-1]:
                output_lines.append('<ul class="nested-list">')
                list_stack.append(indent_len)
            elif indent_len < list_stack[-1]:
                while list_stack and indent_len < list_stack[-1]:
                    output_lines.append("</ul>")
                    list_stack.pop()
                if not list_stack:
                    output_lines.append('<ul class="portal-list">')
                    list_stack.append(indent_len)
                    
            output_lines.append(f"<li>{content}</li>")
        else:
            while list_stack:
                output_lines.append("</ul>")
                list_stack.pop()
                
            if (stripped and not stripped.startswith("<h") and not stripped.startswith("<hr") 
                and not stripped.startswith("<blockquote") and not stripped.startswith("<table") 
                and not stripped.startswith("<thead") and not stripped.startswith("<tbody") 
                and not stripped.startswith("<tr") and not stripped.startswith("<td") 
                and not stripped.startswith("<th") and not stripped.startswith("</table") 
                and not stripped.startswith("</tbody") and not stripped.startswith("</thead") 
                and not stripped.startswith("</tr")):
                # Apply italics in paragraphs
                p_text = re.sub(r"(?<!\*)_([^_]+)_(?!\*)", r"<em>\1</em>", stripped)
                output_lines.append(f"<p>{p_text}</p>")
            else:
                output_lines.append(line)
                
    while list_stack:
        output_lines.append("</ul>")
        list_stack.pop()
        
    result = "\n".join(output_lines)
    
    # 9. Restore code blocks
    for placeholder, code_html in code_blocks.items():
        result = result.replace(placeholder, code_html)
        
    return result





def build_preview():
    if SITE_DIR.exists():
        shutil.rmtree(SITE_DIR)
    SITE_DIR.mkdir(parents=True)
    
    # Copy assets
    assets_src = REPO_ROOT / "assets"
    assets_dest = SITE_DIR / "assets"
    if assets_src.exists():
        shutil.copytree(assets_src, assets_dest)
        
    # Read layout files
    header_html = (REPO_ROOT / "_includes" / "header.html").read_text(encoding="utf-8").replace("{{ site.baseurl }}", "").replace("{{ site.title }}", "The Cybersecurity Trade Project")
    sidebar_html = (REPO_ROOT / "_includes" / "sidebar.html").read_text(encoding="utf-8").replace("{{ site.baseurl }}", "")
    footer_html = (REPO_ROOT / "_includes" / "footer.html").read_text(encoding="utf-8")
    layout_template = (REPO_ROOT / "_layouts" / "default.html").read_text(encoding="utf-8")
    
    import time
    ts = str(int(time.time()))
    layout_shell = layout_template.replace("{% include header.html %}", header_html)
    layout_shell = layout_shell.replace("{% include sidebar.html %}", sidebar_html)
    layout_shell = layout_shell.replace("{% include footer.html %}", footer_html)
    layout_shell = layout_shell.replace("{{ site.baseurl }}", "")
    layout_shell = layout_shell.replace("{{ site.time | date: '%s' }}", ts)
    layout_shell = layout_shell.replace("{{ site.title }}", "The Cybersecurity Trade Project")
    layout_shell = layout_shell.replace("{{ site.description }}", "Restructuring cybersecurity into a recognized skilled trade.")
    
    # Scan and compile all markdown files
    md_files = list(REPO_ROOT.glob("**/*.md"))
    for md_path in md_files:
        if "rfcs" in md_path.parts or ".github" in md_path.parts or "tmp" in md_path.parts:
            continue
        rel = md_path.relative_to(REPO_ROOT)
        dest_rel = rel.with_suffix(".html")
        if rel.name == "README.md":
            dest_rel = rel.parent / "index.html"
            
        dest_path = SITE_DIR / dest_rel
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        
        md_text = md_path.read_text(encoding="utf-8")
        body_html = md_to_html(md_text)
        
        page_html = layout_shell.replace("{{ content }}", body_html)
        dest_path.write_text(page_html, encoding="utf-8")
        
    generate_search_index(md_files)
    print(f"[+] Local preview site generated at: {SITE_DIR}")
    print("[*] To view preview, run: python3 -m http.server 8000 --directory _site")


if __name__ == "__main__":
    build_preview()
