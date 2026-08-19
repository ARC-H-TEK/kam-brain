#!/usr/bin/env python3
"""Secret scan.

Walks the repo and asserts that no API keys, OAuth tokens, session files,
or other secrets are present. The patterns are intentionally conservative:
false positives are fine, false negatives are not.
"""


import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
SKIP_DIRS = {".git", ".github", "node_modules", "venv", ".venv"}

# Patterns that suggest a leaked secret. The check is conservative.
PATTERNS = [
    (r"AIza[0-9A-Za-z\-_]{35}", "google_api_key"),
    (r"sk-[A-Za-z0-9]{20,}", "openai_sk_key"),
    (r"ghp_[A-Za-z0-9]{30,}", "github_pat"),
    (r"github_pat_[A-Za-z0-9_]{50,}", "github_fine_grained_pat"),
    (r"nvapi-[A-Za-z0-9\-_]{20,}", "nvidia_nim_key"),
    (r"xox[baprs]-[A-Za-z0-9\-]{10,}", "slack_token"),
    (r"\d{8,}:AA[A-Za-z0-9\-_]{30,}", "telegram_bot_token"),
    (r"-----BEGIN [A-Z ]*PRIVATE KEY-----", "private_key"),
    (r"AKIA[0-9A-Z]{16}", "aws_access_key"),
    (r"AIza[0-9A-Za-z\-_]{35}", "google_api_key"),
    (r"Bearer\s+[A-Za-z0-9\-_\.]{40,}", "bearer_token"),
]

# Files that may legitimately contain pattern-like text (CI config, examples)
EXT_SKIP = {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".zip", ".ico", ".lock"}

results = []


def check(name: str, ok: bool, detail: str = "") -> None:
    results.append({"check": name, "status": "pass" if ok else "fail", "detail": detail})


def main() -> int:
    findings = []
    file_count = 0
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        if any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts):
            continue
        if p.suffix.lower() in EXT_SKIP:
            continue
        if p.stat().st_size > 5_000_000:
            continue  # Skip large files
        file_count += 1
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        for pattern, label in PATTERNS:
            if re.search(pattern, text):
                findings.append(f"{p.relative_to(ROOT)}: {label}")

    if findings:
        check("secrets.none_found", False, f"{len(findings)} matches: " + "; ".join(findings[:5]))
    else:
        check("secrets.none_found", True, f"scanned {file_count} files")

    print(json.dumps(results, indent=2))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
