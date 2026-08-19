# KAM Brain

> A autonomous digital second-brain system for an individual operator — coordinating trading, freelancing, language learning, and personal growth under one explicit charter.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Charter: v4.1](https://img.shields.io/badge/Charter-v4.1-blue.svg)](CHARTER.md)
[![Status: Public Portfolio](https://img.shields.io/badge/Status-Public%20Portfolio-green.svg)]()
[![Built by: KAM](https://img.shields.io/badge/Built%20by-KAM%20Operator-purple.svg)]()

---

## What is this?

**KAM Brain** is the public, portfolio-facing mirror of a private autonomy system that I've been running since April 2026. It is one half of a two-track split:

- **Public (this repo):** charter, architecture, safety constraints, revenue channels, portfolio of capabilities, and engineering artifacts. Everything here is safe to publish.
- **Private:** operational state, trade journals, decisions, the live chat with the operator, secrets, audit logs. That half stays in a local vault.

The split is intentional. The repo you are reading is a **signal** — it tells you what kind of system I am building, what I will and will not do, and what I have shipped. It is not the live system.

## Who is it for?

Three audiences.

1. **Recruiters / clients** who want to evaluate the engineering and operational work without granting access to private infrastructure. The portfolio page is the entry point.
2. **Engineers** who want to study the architecture — multi-agent gates, charter-driven policy enforcement, subagent fallback patterns, and the KAM/Vault/Hermes isolation model.
3. **The operator** (me) — a single source of truth for the system, even when my private notes drift or get reorganized.

## Charter in one minute

The single rule is:

> **Make money. Everything else is subordinate to that.**

Read [CHARTER.md](CHARTER.md) for the full v4.1 document. The short version:

- **Money first.** Direct revenue > cost-cut > learning/prep.
- **Three gates.** 🟢 self-implement. ⚠️ operator-approval (90s Telegram timeout). 🔴 hard-stop (charter-protection, no override).
- **Hard constraints are not negotiable.** Cracked EA, martingale/grid, msimg32.dll import, equity <10%, and the operator's "**Bauleister**" work hours (06:30–17:00 Europe/Berlin) all trigger automated shutdown even if the operator is asked to bypass them.
- **Approval protocol.** When the system needs a human decision, it asks via Telegram with a 90-second timeout. If the operator does not respond, the system falls back to the charter, not the other way around.

The charter is enforced by `[HARD CONSTRAINT]`-tagged code paths in the agent runtime. The system must refuse to proceed even when explicitly told to.

## Architecture in one diagram

```
                  ┌──────────────────────────┐
                  │  KAM Brain (this repo)   │  Public portfolio
                  │  charter / docs / skills │
                  └──────────────────────────┘
                                ▲
                                │ mirror (publish only)
                                │
       ┌────────────────────────┴────────────────────────┐
       │                                                  │
       │           LOCAL PRIVATE INFRASTRUCTURE          │
       │                                                  │
       │  ┌──────────────┐   ┌────────────────────────┐  │
       │  │   KAM Agent  │   │      Hermes Agent      │  │
       │  │  (operator   │◄──┤  (gateway + cron +     │  │
       │  │   assistant) │   │   subagent dispatch)   │  │
       │  └──────────────┘   └────────────────────────┘  │
       │          │                      │                 │
       │          ▼                      ▼                 │
       │  ┌────────────────────────────────────────┐      │
       │  │  Obsidian Vault (Layer 1/2 memory)     │      │
       │  │  + strategy_memory.yaml (trade rules)  │      │
       │  └────────────────────────────────────────┘      │
       │          │                      │                 │
       │          ▼                      ▼                 │
       │   ┌────────────┐        ┌──────────────┐         │
       │   │  MT5 (DEMO │        │  Telegram /  │         │
       │   │  + REAL)   │        │  Zapier /    │         │
       │   │  XM 88883353│       │  GitHub /    │         │
       │   └────────────┘        │  Notion /    │         │
       │                         │  firecrawl   │         │
       │                         └──────────────┘         │
       └───────────────────────────────────────────────────┘
```

Full breakdown in [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## What lives in this repo

| Path | Purpose |
|---|---|
| [README.md](README.md) | This file. |
| [CHARTER.md](CHARTER.md) | The full v4.1 charter — single rule, three gates, hard constraints. |
| [LICENSE](LICENSE) | MIT. |
| [SECURITY.md](SECURITY.md) | How to report vulnerabilities. |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | Operator covenant. |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to propose changes. |
| [.gitignore](.gitignore) | What never gets committed. |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Multi-agent gates, KAM/Vault/Hermes isolation, subagent fallback. |
| [docs/REVENUE-CHANNELS.md](docs/REVENUE-CHANNELS.md) | Freelance, trading, content, premium — current order and constraints. |
| [docs/HARD-CONSTRAINTS.md](docs/HARD-CONSTRAINTS.md) | The 🔴 list — what the system refuses to do, even on request. |
| [docs/SAFETY.md](docs/SAFETY.md) | Trade safety, Bauleister hours, signal-source vetting. |
| [docs/PORTFOLIO.md](docs/PORTFOLIO.md) | What I have built. What I have shipped. What is in progress. |
| [docs/DECISION-LOG.md](docs/DECISION-LOG.md) | Public-facing decisions (no operator PII). |
| [docs/TESTING.md](docs/TESTING.md) | Test strategy and current coverage. |

## What is explicitly NOT in this repo

- The Obsidian Vault. Live memory, trade journal, secrets, chat logs.
- Backtests, raw market data, indicators, brokerage credentials.
- Any `.env` files, API keys, OAuth tokens, or session files.
- The agent's runtime state, prompt scaffolding, or skill loader logic.

Those belong in the private split. The split is enforced by `.gitignore` and a CI check on the public mirror.

## License

MIT. See [LICENSE](LICENSE).

## Contact

`tekdag2944@gmail.com` — operator inbox. Not for scraping. For real humans who have read the charter and want to talk.

---

*This repo is published by the operator. The system that maintains it is the same system described in the charter. Both the repo and the system are subject to the same hard constraints.*
