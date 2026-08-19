#!/usr/bin/env python3
"""Charter integrity check.

Asserts that CHARTER.md contains the three gates, the hard constraints,
the approval protocol, and matches the README's "single rule" claim.
"""


import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
CHARTER = ROOT / "CHARTER.md"
README = ROOT / "README.md"

results = []


def check(name: str, ok: bool, detail: str = "") -> None:
    results.append({"check": name, "status": "pass" if ok else "fail", "detail": detail})


def main() -> int:
    if not CHARTER.exists():
        check("charter.exists", False, str(CHARTER))
        print(json.dumps(results, indent=2))
        return 1

    charter = CHARTER.read_text(encoding="utf-8")
    readme = README.read_text(encoding="utf-8") if README.exists() else ""

    # Charter exists
    check("charter.exists", True)

    # Three gates
    for gate, marker in (
        ("gate.green", "🟢"),
        ("gate.warn", "⚠️"),
        ("gate.red", "🔴"),
    ):
        check(gate, marker in charter)

    # Hard constraints section (§3)
    check("charter.hard_constraints", bool(re.search(r"## §3.*Hard", charter, re.DOTALL)))

    # Approval protocol (§4)
    check("charter.approval_protocol", "## §4" in charter and "90" in charter)

    # Single rule propagation: README and CHARTER both contain "make money"
    check("readme.mentions_single_rule", "make money" in readme.lower() or "para kazan" in readme.lower())
    check("charter.mentions_single_rule", "make money" in charter.lower() or "para kazan" in charter.lower())

    # License
    check("charter.mentions_license", "MIT" in charter or "mit" in charter.lower())

    # Hard constraints list completeness
    for label in (
        "martingale",
        "msimg32.dll",
        "Bauleister",
        "10%",
    ):
        check(f"charter.mentions_{label}", label in charter)

    print(json.dumps(results, indent=2))
    bad = [r for r in results if r["status"] == "fail"]
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
