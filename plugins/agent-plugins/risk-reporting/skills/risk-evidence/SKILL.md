---
name: risk-evidence
description: The auditability guardrail for every digital-asset-risk agent. Every risk claim in every output must carry the Metrika KRI id (or monitor/incident/table/report object id) and its deep-link that supports it. No claim without a reference. Load this whenever producing any risk statement, brief, memo, assessment, or pack.
---

# Cite every risk claim

An auditor reading any output must be able to click straight back to the Metrika object behind each statement. This is non-negotiable.

## The rule

**No risk claim without a reference.** Every sentence that asserts a fact about risk (a value, a trend, a breach, a hit, a rating input) carries:

1. the **object id** — the KRI id, or the monitor / incident / datatable / report id — verbatim, and
2. the **deep-link** (`webUrl`) returned with that object, as a clickable markdown link.

If you cannot attach a reference, you cannot make the claim. Say "not available in Metrika" instead of asserting it.

## Reference format

Inline, human- and audit-readable:

> USDC 24h net bridged outflow reached $X on 2026-07-14, a Yx increase vs the trailing-30d p50 — [Bridging · Volume Bridged](<webUrl>) (`kriId: <verbatim-id>`).

For a table of claims, add an **Evidence** column carrying `kriId` + link. For memos and packs, end with a **Sources** / **Evidence appendix** listing every object id and link used, so the references survive copy-paste out of chat.

## What counts as a reference

- A **KRI** → `kriId` + its `webUrl`, plus the specific statistic used (`last`, `p90`, window). Name the window; "elevated" without a number and a period is not a claim, it's a vibe.
- A **breach / alert** → the incident `id` + `webUrl`, the monitor name, and the breaching rule/threshold from the transition.
- A **holder / sanctions / concentration fact** → the datatable `webUrl` and the row basis (e.g. "top-5 share = Σ of `balance_per` over the top 5 rows").
- A **report answer** → the report `_id` + `webUrl` and the question `order`.

## Numbers discipline

Quote Metrika's values; state units (fractions vs %, native vs USD); don't add significant figures the series doesn't have. When you compute something (a sum, a ratio, a delta), show the inputs so it can be checked. Distinguish a **measured** value from an **estimate** or an **absence of data** — never present a gap as a zero.

## Separate fact from interpretation

Metrika tools return facts. The rating, the "why it matters," the recommended action — those are the agent's interpretation and must be labelled as such, sitting next to (not blended into) the cited facts. The reviewer needs to see where the data ends and the judgement begins.
