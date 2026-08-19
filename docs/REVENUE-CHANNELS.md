# Revenue channels

The charter §5 ranks revenue channels by priority. This file describes each channel, the constraints it operates under, and what "done" looks like.

## 1. Freelance / task

**Priority:** highest.

**Channels:**

- **MQL5 Marketplace** — sell EAs, indicators, scripts. Open-source only (no cracked EA, no `msimg32.dll` import, no martingale/grid). Source-code-reviewable.
- **Bug bounty** — public platforms, charter-compliant programs only. No customer data exfiltration, no social engineering.
- **Marketplace scraping** — automated job discovery from freelancer sites. Filter, rank, propose. No customer data stored.

**Constraints:**

- No crack / no jailbreak / no pirated tool. The marketplace is for original work only.
- No customer data retention. The agent logs engagement, not user data.
- Each application is logged. The agent does not spam.

**Done looks like:**

- ≥ 1 marketplace listing live (MQL5 or equivalent)
- ≥ 1 bug bounty submitted
- Weekly pipeline review with the operator

## 2. Trading

**Priority:** second.

**Strategy:** XAUUSD Bollinger Band 15m mean reversion.

**Phases:**

1. **Dry-run** — backtest + paper trade. Mandatory before any live order.
2. **Operator approval** — charter §2 ⚠️ gate. 90s Telegram timeout.
3. **Live** — single position, single symbol, ATR-based SL/TP, no martingale, no grid.

**Constraints:**

- Charter §3 hard stop on equity < 10%.
- Charter §2 ⚠️ hard approval for every live order.
- Charter §3 Bauleister hours block (06:30–17:00 Europe/Berlin).
- Charter §3 hard stop on any strategy with martingale / grid / recovery / avg-down.

**Risks acknowledged:**

- Single-strategy, single-symbol concentration.
- Broker dependency (XM MT5).
- Slippage and requote on real money.

**Done looks like:**

- Backtest with documented assumptions.
- Paper trade with at least 100 trades logged.
- Live approval flow exercised at least once.
- Strategy memory record with status.

## 3. Telegram premium

**Priority:** third.

**Channels:** charter-compliant Telegram channels. Read + DM notification.

**Constraints:**

- Charter §3 — no cracked groups. No martingale signals. No "guaranteed" win claims.
- Salt-read-only observer. The agent does not auto-trade.
- DM notification per observed message. The agent is a messenger, not a signal source.

**Done looks like:**

- ≥ 1 channel observed with consistent signal quality.
- Operator has exercised manual approval on ≥ 1 signal.
- Audit log shows every signal + operator decision.

## 4. YouTube

**Priority:** fourth.

**Content:** Turkish-language AI tutorials. Built with Comfy Cloud image generation, voice synthesis, and a script pipeline.

**Constraints:**

- No private data in published content.
- No charter-violating strategy content (no martingale, no cracked EA).
- Disclose AI generation in published metadata.

**Done looks like:**

- ≥ 1 video published.
- Documented pipeline (idea → script → voice → image → assembly → publish).
- Loop back to charter §5 — content is revenue, not vanity.

## 5. Cost-cut

**Priority:** lowest.

**Purpose:** defensive. The agent refuses paid services, recycles what it has, and prefers self-hosted.

**Done looks like:**

- No recurring SaaS expense in the agent's tracker.
- All free-tier quotas monitored.
- Every "vendor X" request defaults to "do we self-host instead?"

## What is explicitly not a channel

- **Subscription resale.** No bundling free signals into a paid product.
- **Affiliate marketing.** The agent does not insert referral links.
- **NFT / token / DeFi.** Out of scope. The charter is about revenue, not speculative upside.
- **Reselling customer data.** Charter §3 hard stop.

## How a new channel gets added

The operator adds channels. The agent does not propose new channels. The pipeline is:

1. Operator describes the channel.
2. Agent reports constraints and risks.
3. Operator approves.
4. Agent implements, logs, monitors.

This is documented in [docs/DECISION-LOG.md](DECISION-LOG.md).

---

*The priority order is not a hint. It is the order the agent allocates effort. Lower-priority channels are not "done" — they are deferred.*
