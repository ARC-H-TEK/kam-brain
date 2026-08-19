# Security Policy

## Supported versions

This is a portfolio mirror of a private autonomy system. The public repo is documentation-first; there is no production binary to patch. Security here means:

- the integrity of the published charter and architecture
- the absence of accidental secret leaks
- the absence of supply-chain attacks on the documentation

## Reporting a vulnerability

If you find a security issue in this repo (e.g. a leaked credential, a malicious link, a supply-chain compromise), please email:

**tekdag2944@gmail.com**

Please do:

- Describe the issue with enough detail to reproduce.
- Include any URLs or commit SHAs involved.
- Wait for an acknowledgement before disclosing publicly.

Do not:

- Open a public GitHub issue for a credential leak or vulnerability.
- Use the issue tracker for security-sensitive disclosures.

## Response timeline

- **Acknowledge:** within 72 hours.
- **Triage:** within 1 week.
- **Fix or document mitigation:** as soon as practical, depending on severity.

## Hard constraints (from the charter)

The charter v4.1 §3 is binding on the system that maintains this repo:

- No `msimg32.dll` import or any opaque DLL chain in any code I publish.
- No cracked EAs, no cracked Telegram groups, no martingale/grid/recovery patterns.
- No live trading without operator approval.
- No public release of credentials, tokens, or session files.

If you spot a violation of these constraints in a published artifact, please report it.
