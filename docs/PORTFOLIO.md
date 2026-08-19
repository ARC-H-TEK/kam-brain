# Portfolio

What this system has built. What it has shipped. What is in progress. One operator, one charter, many artifacts.

Last updated: 2026-08-19.

## Engineering

### Charter-driven autonomy runtime

A long-running agent with an explicit charter loaded at every session, three authority gates (🟢 self / ⚠️ approval / 🔴 hard-stop), and a 90-second approval timeout that falls back to the charter, not the request.

- **Status:** in production.
- **Version:** charter v4.1.
- **Public artifact:** [CHARTER.md](../CHARTER.md), [docs/ARCHITECTURE.md](ARCHITECTURE.md).

### Strategy memory + decision engine

A versioned record of every strategy the agent has tried, with backtest, paper, and live phases, and a 6-step decision engine (research → analyze → score → decide → implement → monitor) with a charter-integrated ROI gate.

- **Status:** in production.
- **Records:** N strategies in `strategy_memory.yaml` (private).
- **Public artifact:** [docs/REVENUE-CHANNELS.md](REVENUE-CHANNELS.md).

### Subagent fallback chain

When subagents 404 or 429, the agent pivots to direct MCP tools. The pivot is logged. The fallback chain is configurable per session.

- **Status:** in production.
- **Default chain:** Nous (subagent) → NVIDIA NIM (subagent) → MCP direct (Obsidian REST, GitHub, Telegram).
- **Pitfalls documented:** tool-layer credential masking, subagent self-report verification.

### Cron-based watchdog pattern

Long-running `cronjob` instances with `monitor_script` for change detection. The hash-suppression semantics mean unchanged output is a silent no-op — only changes trigger the agent.

- **Status:** in production. Multiple watchdog jobs running.
- **Example:** charter-violation monitor, broker-equity watcher, daily audit producer.

### Telegram gateway with charter-aware routing

Built-in Telegram gateway that enforces Bauleister hours (06:30–17:00 Europe/Berlin), routes through topic-aware message handling, and refuses to act on cracked-channel messages.

- **Status:** in production.
- **Channels observed:** 1+ vetted trader channels (salt-read-only), DM notifications.
- **Pitfall documented:** Telethon forum-filter parameter (`reply_to=msg_id` not `top_id`).

### Salt-read-only signal observer

For Telegram channels that pass the charter's signal-source vetting: parse messages, log every signal, do not trade without operator approval. The agent is a messenger, not a signal source.

- **Status:** in production.
- **Audit log:** one JSONL line per message with verdict + reason.

## Trading

### XAUUSD Bollinger Band 15m mean reversion

Single-strategy, single-symbol mean reversion. ATR-based SL/TP direction-safe, no martingale, no grid.

- **Phase:** dry-run → live approval flow planned.
- **Backtest:** documented with synthetic-tick isolation caveat.
- **Public artifact:** charter §3 + §5.

### Trailing stop manager (`KAM_TrailingManager.mq5`)

A global trailing-stop manager EA. Per-symbol pip distance (EURUSD 30, XAUUSD 100, BTCUSD 200, US30 80). Costs (commission + swap) added to SL distance. Charter-compliant (trailing is risk-management, not martingale).

- **Status:** compiled and running on operator's MT5.
- **Built:** 2026-08-13.

## Language

### Telc C1 preparation system

A German C1 exam preparation system, running autonomously. Daily quiz, weekly mock test, error log + SRS. Target: October 2026.

- **Status:** in production (KAM-OTONOM mode).
- **Sources:** telc C1 official, Schubert Verlag, Cornelsen, online Hörtraining.
- **Constraint:** UDE Hörerstatus, not regular student — DAAD / Türk-Alman Vakfı / Avicenna burs options.

## Sites

### kamversicherung.de

A German insurance brokerage site. Hugo static site, Blowfish theme.

- **Status:** live, contact form, Impressum, Datenschutz.
- **Pipeline:** marketing copy → Hugo → GitHub → Cloudflare Pages.

### kamversicherung-hugo

The Hugo source for kamversicherung.de.

- **Status:** in production.

## Integrations

### 8+ API integrations

| Service | Use | Mode |
|---|---|---|
| GitHub | repo, PR, issue | full |
| Telegram | gateway, observers, alerts | full |
| Zapier | 147 tools, Gmail/Calendar/Docs/Sheets | full |
| NVIDIA NIM | delegation | full |
| Nous Portal | subagent delegation | full |
| Obsidian REST | vault read/write | full |
| OpenRouter | subagent fallback | full (free tier) |
| Pinokio | local LLM (self-hosted) | full |

### Zero paid tier

The full stack runs on free tiers + self-hosted. No recurring SaaS expense. Charter §5-channel-5 priority.

## Code

### Skills

A library of loaded skills covering telc prep, AI-loop engineering, RAG over the vault, MT5 safety, Telegram userbot ops, MT5 live-bot ops, cron auto-doctor, vault-RAG, vault memory prompts, freelance opportunity scanning, video pipelines, and trading strategy factory.

- **Count:** 30+ skills loaded.
- **Source:** private `~/.hermes/skills/`.

### Public portfolio

This repo (kam-brain) is the public-facing artifact. Published from private to public via `git` push; the private mirror is the source.

## In progress

- **Live trading go-live.** Dry-run + paper-trade phases complete. Operator approval flow being exercised.
- **YouTube channel for Turkish AI tutorials.** Pipeline built, first video in production.
- **MQL5 marketplace listing.** First EA in review.
- **Council / YDK governance.** Charter §6 governance loop being formalized.

## What is not on this page

- Live account balance, open positions, P&L.
- Real-time signal flow.
- Operator PII beyond the public-record name.
- Private vault contents.

For what is in the private mirror, the operator can be contacted at `tekdag2944@gmail.com`.

---

*The portfolio is a snapshot. The numbers in the private mirror are younger. The portfolio is the public claim. The mirror is the proof.*
