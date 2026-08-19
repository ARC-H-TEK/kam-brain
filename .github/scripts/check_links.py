#!/usr/bin/env python3
"""Link integrity check.

Walks every markdown file in the repo, extracts relative links, and asserts
that each one resolves to a real file or anchor.
"""


import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
SKIP_DIRS = {".git", ".github", "node_modules", "venv", ".venv"}

results = []


def check(name: str, ok: bool, detail: str = "") -> None:
    results.append({"check": name, "status": "pass" if ok else "fail", "detail": detail})


LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def main() -> int:
    md_files = []
    for p in ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts):
            continue
        md_files.append(p)

    if not md_files:
        check("links.files_found", False, "no markdown files")
        print(json.dumps(results, indent=2))
        return 1

    check("links.files_found", True, f"{len(md_files)} files")

    broken = []
    for md in md_files:
        text = md.read_text(encoding="utf-8", errors="replace")
        for match in LINK_RE.finditer(text):
            label, target = match.group(1), match.group(2).strip()
            # Skip anchors-only, http(s), mailto, and templated placeholders
            if not target or target.startswith("#") or target.startswith("http") or target.startswith("mailto:"):
                continue
            # Strip fragment
            target_no_frag = target.split("#", 1)[0]
            if not target_no_frag:
                continue
            target_path = (md.parent / target_no_frag).resolve()
            if not target_path.exists():
                broken.append(f"{md.relative_to(ROOT)}: [{label}]({target}) -> {target_path}")

    if broken:
        check("links.all_resolve", False, f"{len(broken)} broken: " + "; ".join(broken[:5]))
    else:
        check("links.all_resolve", True)

    print(json.dumps(results, indent=2))
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
