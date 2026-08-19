# Architecture

The system is a single-operator autonomy stack built from three components that are isolated by design:

```
        ┌─────────────────────────────────────────────┐
        │              KAM (operator agent)           │
        │  - charter-aware reasoning                  │
        │  - 17-layer memory                           │
        │  - approval protocol (90s timeout)          │
        └────────────────┬────────────────────────────┘
                         │
                         ▼
        ┌─────────────────────────────────────────────┐
        │           Hermes Agent (gateway)            │
        │  - cron scheduler                           │
        │  - Telegram / Discord / Slack gateway       │
        │  - subagent dispatch (delegation)           │
        │  - tool routing (mcp / function / shell)    │
        └────────────────┬────────────────────────────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
   ┌─────────┐     ┌──────────┐    ┌────────────┐
   │  Vault  │     │  MT5 /   │    │  Telegram  │
   │ Obsidian│     │  Trade   │    │  / Zapier  │
   │ (memory)│     │ Memory   │    │  / GitHub  │
   └─────────┘     └──────────┘    └────────────┘
```

Read top-down: KAM is the agent that the operator interacts with. Hermes is the gateway that runs the cron, dispatches subagents, and routes tools. The lower three are the integration layers.

## KAM (operator agent)

The reasoning layer. KAM is instantiated as a long-running session with:

- **Charter awareness.** The charter v4.1 is loaded at the top of every session. The agent cannot proceed on a request that violates a hard constraint.
- **17-layer memory.** Operational pointers, plus a structured layer model (Layer 1 private, Layer 2 linked). The vault is the substrate; the layers are the access tiers.
- **Approval protocol.** For ⚠️ -gated actions, the agent asks via Telegram with a 90-second timeout. If the operator does not respond, the agent falls back to the charter, not to the request.

## Hermes Agent (gateway)

The execution layer. Hermes handles:

- **Cron schedule.** `cronjob` runs local scripts at scheduled times. The agent does not sleep; it does run scheduled tasks.
- **Telegram / Discord / Slack gateway.** Fetching messages, sending replies, observing channels. The gateway is process-internal — there is no separate bot daemon.
- **Subagent dispatch.** `delegate_task` spawns isolated subagents with their own context. Subagent outputs are self-reports; the parent verifies before acting.
- **Tool routing.** `mcp__*`, `function_call`, `terminal`, `web_search`, `read_file`, `write_file`, `patch`. The gateway is the registry.

### Single-process platform

Hermes is one process. The Telegram gateway is built into the same Python process that runs `cronjob` and `dispatch`. There is no separate "bot" script. A `kam_bridge` / `kam_bot_watcher` script from older versions is legacy and not used.

## Vault (Obsidian)

The persistence layer. The vault is a local Obsidian folder with this structure:

```
KAM-Vault/
├── 00_Agent_Instructions.md
├── 00_Index/
├── 01_Self/
├── 02_Projects/
├── 03_KAM_System/
├── 04_Memory/
├── 05_Domains/
├── 06_Scripts/
├── 07_Brain/
├── 08_Decisions/
├── 09_Procedures/
├── 10_Archive/
├── 11_Skills/
├── 12_Autonomy/
├── 13_Context_Graph/
├── 14_Media/
├── 15_Audit/
├── 16_Connectors/
├── 17_Vault_Refs/
├── 18_Templates/
├── 19_Reports/
├── 20_Roadmaps/
├── 21_System/
├── 22_Telegram_Sync/
├── 23_Competitors/
├── 24_Optimization/
├── 25_Sales/
├── 30_Trading/
└── 99_Archive/
```

### Layer 1 / Layer 2 model

- **Layer 1** — private. The operator's own notes, draft thoughts, partial logs. `.gitignore` excluded from the public mirror.
- **Layer 2** — linked. Curated, linked, version-controlled. This is what the public mirror is drawn from.

The layer is enforced by a combination of `.gitignore` patterns and a CI check that scans for layer-1 markers in the public mirror.

### Strategy memory

`strategy_memory.yaml` (in the private vault) is a versioned record of every trading strategy the agent has tried, with:

- Strategy description
- Indicator set
- Risk profile
- Backtest results (with caveats)
- Live test results
- Status (active / paused / killed)

The strategy memory is referenced — not copied — in the public portfolio.

## MT5 / Trade Memory

MT5 is the broker integration. XM MT5 88883353 is the live account. Trade Memory is the audit layer that records every decision (signal, gate, outcome) and reconciles it against the broker state.

The integration is **read-only by default**. Order placement is gated by:

- Charter §3 (no martingale, no grid, no recovery)
- Charter §2 ⚠️ (live trade requires operator approval)
- Charter §3 (Bauleister hours block)

Order placement is implemented as a deny-by-default function. The agent's MT5 module will refuse to send an order unless:

1. The signal has been logged.
2. The operator has approved via the 90s protocol.
3. The current time is outside Bauleister hours.
4. Equity is above the 10% panic threshold.

## Telegram / Zapier / GitHub

External integrations are brokered via MCP when available, fall back to REST when MCP is unavailable.

- **Telegram** — built-in gateway. Salt-read-only observers for specific channels (audit requirement: DM notification on every message).
- **Zapier** — 147 tools, including Gmail, Calendar, Docs, Sheets. Used for low-risk automation.
- **GitHub** — repo management, PR review, issue triage. The public repo is published through this integration.

## Subagent fallback

When subagents 404 or 429 (rate-limit), the agent pivots to direct MCP tools. The pivot is logged.

A typical example:

```
subagent: 429 NVIDIA NIM
  ↓
agent: pivot to nous:deepseek-v4-pro
  ↓
subagent: 404
  ↓
agent: pivot to MCP direct call (Obsidian REST API)
```

The fallback chain is configurable per session. The default chain is documented in the private vault.

## Charter enforcement

The charter is enforced at three levels:

1. **Prompt-level** — the charter is loaded at the top of every session. The agent reads it before reasoning.
2. **Tool-level** — `[HARD CONSTRAINT]`-tagged code paths refuse to execute on invalid input. The agent cannot bypass by editing prompts.
3. **Audit-level** — every gate decision is logged. The audit log is the source of truth when behavior and charter disagree.

The agent cannot be told to violate the charter. The operator cannot be asked to violate the charter on the agent's behalf. Both halves of the system know this.

## What is intentionally not documented here

- **Secrets.** No API keys, tokens, OAuth credentials, session files, or brokerage hashes. See `.gitignore`.
- **Live state.** No current positions, P&L, account balance, or active signal. The portfolio page uses historical, not real-time, data.
- **Operator PII.** The full name in the header is public-record (LinkedIn-level). Address, phone, ID numbers, and account numbers are not in this repo.

---

*Architecture is the part of the system that lives in the operator's head. The doc is the part that lives in the public mirror. Both are kept in sync by the same agent that runs the system.*
