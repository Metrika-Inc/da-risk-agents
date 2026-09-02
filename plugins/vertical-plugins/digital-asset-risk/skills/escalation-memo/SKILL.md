---
name: escalation-memo
description: Draft a concise escalation memo from a triaged incident or risk situation — for a human to review, adjust, and send. States the situation, evidence, proposed severity, impact, and options/next steps, with a full evidence appendix. Never sends or escalates anything itself. Requires metrika-mcp, risk-evidence, review-gate.
---

# Escalation memo (draft)

A short, decision-oriented memo the reviewer can edit and forward. You draft it; a named human owns and sends it.

## Inputs
A triaged incident/situation (ideally from `incident-triage`) and the intended audience (desk lead, risk committee, CRO). Re-pull any evidence you cite so the memo is self-contained.

## Structure

1. **Status banner** (from `review-gate`) — makes clear this is a draft for sign-off, not an issued escalation.
2. **Subject** — entity, one-line what-happened, proposed severity (labelled *proposed*).
3. **Situation** — 2–4 sentences: what breached, when, how far past threshold. Cited.
4. **Evidence** — the corroborating facts as bullets, each with `kriId`/incident id + `webUrl`. Note what agrees and what doesn't.
5. **Assessment** — the agent's read, explicitly separated from the facts: severity rationale, signal-vs-noise, confidence.
6. **Potential impact** — what's exposed if this is real (framed as scenario, not certainty).
7. **Options / recommended next step** — 2–3 courses of action for the human to choose among, each with a trade-off. Framed as options, never as an executed instruction.
8. **Owner & decision needed** — who must decide and what the specific ask is (blank owner field for the human to fill).
9. **Evidence appendix** — every Metrika object id + deep-link used, so references survive outside chat.

## Discipline
Lead with the decision the reader must make. Keep it under a page. No unreferenced claim. Distinguish measured impact from hypothetical. Do not pre-fill the sender, approvals, or a "sent" status — those are the human's. If evidence is thin, the memo says "provisional — pending X," it does not inflate confidence to look complete.
