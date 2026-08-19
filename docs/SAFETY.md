# Safety

The charter is the policy. This file is the engineering. The hard constraints are not a wish — they are codepath conditions.

## Threat model

The agent operates in an environment where:

- **The operator's wallet is reachable.** MT5 live account, brokerage credentials in scope.
- **The operator's data is reachable.** Gmail, Calendar, Drive, Notion, GitHub — all in scope for content.
- **External sources are hostile by default.** Telegram groups, marketplace listings, freelance gigs — all treated as potentially adversarial.

The safety model assumes breach. The agent designs for the case where any single integration is compromised.

## Defense in depth

### Layer 1 — prompt-level

The charter is loaded at the top of every session. The agent reads it before reasoning. This is the most fragile layer because it is text — but it is also the most flexible.

### Layer 2 — tool-level

`[HARD CONSTRAINT]`-tagged code paths refuse to execute on invalid input. The agent cannot bypass by editing prompts because the bypass is a code path, not a prompt path.

Examples:

- `martingale_check(strategy)` — refuses to accept a strategy with martingale properties
- `msimg32_scan(ea_path)` — refuses to load an EA with `msimg32.dll` import
- `bauleister_hours_block(now)` — refuses to act on a trade request during the block
- `equity_panic_stop(equity, starting)` — forces close-and-halt on equity < 10%

### Layer 3 — audit-level

Every gate decision is logged. The audit log is the source of truth when behavior and charter disagree. The log is append-only and versioned.

## Build hazards

### Web sources

- **Telegram groups.** Salt-read-only observer. The agent parses messages but does not act on them automatically. Every observed message requires operator approval before any trade.
- **Marketplace listings.** The agent does not auto-purchase. The agent does not store customer payment data.
- **Web search.** The agent uses it for research. The agent does not paste URLs into decisions without verification.

### Tool sources

- **`terminal`.** The agent runs commands. The agent does not run commands from external sources without operator review.
- **`execute_code`.** The agent runs Python. The agent does not run code from external sources without operator review.
- **`delegate_task`.** Subagent outputs are self-reports. The agent verifies before acting — for any side-effect, the agent fetches the URL or `stat()`s the file.

### Memory sources

- **Memory.** The agent has injection-detection. Any embedded instruction in tool output that tries to override the agent's charter is logged and ignored.
- **Vault.** The vault is local. The agent does not merge external pull requests into the vault automatically.

## Failure modes

### Subagent hallucination

Subagents can claim success without doing the work. The agent verifies:

- File writes — `stat()` the path, confirm size.
- Web uploads — fetch the URL, confirm 200.
- API calls — re-check with `GET`.

### Token leak

Secrets are loaded from `~/.hermes/secrets/*` and never pasted into commands. The agent uses environment variables or Python file reads, not shell-arg secrets.

### Model drift

The agent's model can be changed by the operator. The agent detects the change and re-loads the charter. The change is logged.

### Prompt injection

Any text that arrives from an external source is treated as data, not instructions. The agent:

- Quotes, not acts, on suspicious content.
- Logs the injection attempt.
- Does not propagate to the operator's other channels.

### Operator sleep

The agent does not assume the operator is awake. Telegram responses that arrive during the Bauleister block are queued and digested at block end. The 90-second approval timeout is a feature, not a bug.

## Incident response

When a hard constraint fires:

1. The agent refuses.
2. The refusal is logged.
3. The operator is notified.
4. The agent suggests the closest charter-compliant alternative.

When a soft constraint fires:

1. The agent asks the operator.
2. The operator has 90 seconds to respond.
3. After 90 seconds, the agent falls back to the charter.

When a model or tool misbehaves:

1. The agent catches the deviation.
2. The agent logs it.
3. The agent pauses the affected subsystem.
4. The agent notifies the operator.

## What the agent does not do

- **Auto-trade.** Never. The agent does not execute trades without operator approval. Charter §2 ⚠️.
- **Auto-spend.** Never. The agent does not initiate purchases without operator approval.
- **Auto-email-send.** The agent drafts but does not send email without operator approval on the draft.
- **Auto-publish.** The agent drafts but does not publish to GitHub, YouTube, or marketplace without operator approval on the draft.
- **Auto-message.** The agent does not message other humans without operator approval on the message.

## What the agent does

- **Auto-archive.** The agent moves content to vault, indexes, archives logs, updates decision records.
- **Auto-monitor.** The agent watches scheduled channels, file paths, and account state for changes.
- **Auto-draft.** The agent produces drafts that the operator reviews.
- **Auto-flag.** The agent notifies the operator on any hard-constraint firing, any rate-limit, any tool failure.

## The Đ0 — the daily audit

Every day, the agent produces a daily audit:

- All charter-firing events.
- All subagent outputs verified (or unverified).
- All Telegram messages received and acted on.
- All MT5 signals + gate decisions.
- All cron jobs run + outcomes.
- All vault writes.

The daily audit is appended to the operator's `journal/daily/` folder in the private vault. The public mirror does not include the daily audit.

---

*Safety is not a feature. It is the substrate. The agent exists inside the safety model, not the other way around.*
