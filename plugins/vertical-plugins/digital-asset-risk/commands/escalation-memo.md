---
description: Draft an escalation memo from a triaged incident for a human to review, edit, and send (read-only)
argument-hint: "[incident id | triaged situation] [audience]"
---

# /escalation-memo

Draft a concise, decision-oriented escalation memo. **You draft it; a named human owns and sends it.**

1. Load `review-gate`, `metrika-mcp`, `risk-evidence`, then `escalation-memo`.
2. If not already triaged, run `incident-triage` first.
3. Re-pull cited evidence so the memo is self-contained; follow the `escalation-memo` structure.
4. Output opens with the DRAFT banner; ends with an evidence appendix (object ids + deep-links). Options, not instructions; owner/sender fields left blank for the human.

Read-only. Nothing is sent or escalated by the agent.
