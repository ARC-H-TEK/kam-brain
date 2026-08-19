# Testing

Testing strategy for the public mirror. The private runtime has its own test suite; this document is about what the public repo asserts.

## What the public mirror tests

### 1. Charter integrity

The charter v4.1 is the anchor document. The mirror asserts:

- The charter is valid markdown.
- The charter contains the three gates (🟢 / ⚠️ / 🔴).
- The charter contains the hard constraints (§3).
- The charter references the approval protocol (§4).
- The charter is MIT-licensed.

### 2. README ↔ Charter consistency

The README and the charter must agree on:

- The single rule.
- The hard constraints.
- The revenue channel order.

### 3. Link integrity

Every link in the README, CHARTER, and `docs/` must resolve to a real file in the repo. No 404s.

### 4. Secret scan

No `.env` files, no API keys, no OAuth tokens, no session files in the public mirror. The CI job runs the same secret-scan that the operator uses on the private vault.

## What the public mirror does NOT test

- **Live runtime behavior.** The runtime is private.
- **Trading strategy performance.** Backtests and live results are in the private vault.
- **Subagent output.** Subagent outputs are in the private vault.
- **Operator decisions.** Those are in the private vault.

## CI workflow

The public mirror's CI runs on every push to `main`:

```yaml
name: ci
on: [push, pull_request]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Charter integrity
        run: python .github/scripts/check_charter.py
      - name: Link integrity
        run: python .github/scripts/check_links.py
      - name: Secret scan
        run: python .github/scripts/scan_secrets.py
```

The scripts are pure Python with no external dependencies. They are part of the public mirror.

## Schema

Each test script outputs a JSON line per assertion:

```json
{"check": "charter.gates", "status": "pass", "test": "gates present"}
{"check": "charter.gates", "status": "fail", "test": "missing gate: 🔴"}
```

The CI job exits non-zero on any failure.

## Manual review

For changes that touch `CHARTER.md` or `docs/HARD-CONSTRAINTS.md`:

- The PR is reviewed by the operator.
- The PR body must include the rationale.
- The PR is not auto-merged.

For other documentation changes:

- Auto-merge if CI passes.
- Manual review if the change is structural.

## Why the test suite is small

The public mirror is documentation. The test suite asserts:

1. The documentation is internally consistent.
2. The documentation does not leak secrets.
3. The documentation links resolve.

That is the scope. The runtime tests live in the private vault.

## Future

The CI workflow is intended to grow to include:

- A `git diff` check that the diff between private and public mirrors contains only the public files.
- A spell-check on the English markdown.
- A documentation-coverage check that every section in the table of contents has a real file.

These are aspirational. The current scope is the scope that ships.

---

*Tests are the public claim that the documentation is what it says it is. The CI runs on every change. The operator reviews the charter changes.*
