# Decision log

Curated, public-facing decisions. The full private log is in `08_Decisions/` in the operator's vault. This page is the curated subset.

## 2026-08-18 — Charter v4.1 adopted

**Context:** v4 (single-rule "make money") had been drafted but not implemented. Operating contract v2 had been adopted earlier.

**Decision:** adopt v4.1: same single rule, with §5 revenue channels expanded and §10 SALIH guidance mode added.

**Reason:** simplify the operator's mental model. Group operating rules under one anchor. Make the boundaries explicit.

**Alternative considered:** keep v2.2 + ad-hoc amendments. Rejected because the amendments were drifting.

**Outcome:** charter v4.1 is the binding document. v2.2 archived. v3 draft retired.

## 2026-08-18 — YDK → operator-onay geçişi

**Context:** the YDK (Yüksek Denetleme Kurulu) had been a review gate. The operator requested a shift to direct Telegram approval.

**Decision:** replace YDK review with the 90-second Telegram approval protocol. Council remains as a soft gate for medium-risk changes.

**Reason:** reduce cycle time. The YDK was duplicating operator review.

**Outcome:** risk classification now 🟢 / ⚠️ / 🔴 with the 90s operator timeout as the primary gate.

## 2026-08-19 — Operating contract v2

**Context:** a single operator and a single agent. The operating contract had been treating the agent as one of several agents.

**Decision:** the agent takes full ownership of the operator's revenue mission. Charter v4.1 hard constraints still bind. The agent does not require approval for 🟢 actions.

**Reason:** the operator was bottlenecking on reviews for actions that were already on the charter.

**Outcome:** the agent now self-implements 🟢 actions, asks once on ⚠️, and refuses 🔴.

## 2026-08-19 — Public mirror (this repo)

**Context:** the agent's infrastructure is non-public. The operator's portfolio is public.

**Decision:** publish kam-brain as a public mirror — charter, architecture, hard constraints, revenue channels, portfolio, decision log. Exclude private vault, secrets, runtime state.

**Reason:** the operator's portfolio benefits from being public. The private infrastructure does not.

**Alternative considered:** publish a polished blog post instead. Rejected because the architecture is a living document, and the blog post would be stale within a week.

**Outcome:** this repo is the public artifact. The private vault remains the source of truth.

## Format

Each decision entry includes:

- **Date** — when the decision was made.
- **Context** — what was true at the time.
- **Decision** — what was chosen.
- **Reason** — why that choice.
- **Alternative considered** — what was rejected.
- **Outcome** — what happened.

PII is redacted. Operator-specific identifiers (account numbers, broker hashes, bot tokens) are excluded. The principle is the same as the charter: the public mirror preserves the why, not the how.

## What is not here

- **Trade-by-trade decisions.** Those are in the private vault under `30_Trading/journal/`.
- **Agent prompt iterations.** Those are in the private vault under `03_KAM_System/`.
- **Council / YDK meeting minutes.** Those are in the private vault under `decision-log/`.

## Reader note

If you are reading this from a recruiter's perspective: the decision log is the clearest evidence of how the agent reasons. If you are reading this from an engineer's perspective: the format is inspired by AWS-style "decision records" with the operator-as-customer framing.

---

*The decision log is not a brag. It is a record of what the operator chose, and why. The why is the part that matters.*
