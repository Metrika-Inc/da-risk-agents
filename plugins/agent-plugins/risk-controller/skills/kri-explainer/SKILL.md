---
name: kri-explainer
description: Explain a KRI or a KRI spike in plain language — what the indicator measures, what its recent movement was (with the numbers), plausible drivers corroborated by other Metrika data, and what it does and doesn't imply. Read-only. Use for "why did X spike?" and "what does this KRI mean?". Requires metrika-mcp, risk-evidence, review-gate.
---

# Explain a KRI / KRI spike

Make an indicator legible to a risk reviewer without overclaiming causation.

## Inputs
A KRI id, or a natural-language question + entity. If a question, use `metrika_kri_find_smart` to pick the KRI(s) and carry its `why`.

## Workflow

1. **Define it.** From the KRI catalog record: name, description, `metricName`, native interval, `kriAbstraction.labels`. State what it measures and its units.
2. **Show the movement.** `metrika_kri_get_timeseries` over a window that frames the move (e.g. `90d` to place a spike in context). Report `last`, the peak/trough with dates, and `last` vs `p50`/`p90`. Describe shape: spike, step, drift, seasonal.
3. **Look for drivers — corroborate, don't assume.** Check what could explain the move using *other* Metrika objects in the same window: on-chain datatables (large transfers, mint/burn events, holder/sanctions changes, governance/admin actions, bridge flows), related KRIs, adverse-media incidents. Present each candidate driver with its own citation and how strongly it lines up in time.
4. **Bound the claim.** Say what the KRI does and does not tell you. Correlation in a window is not proof of cause; name the alternative explanations you couldn't rule out.

## Output shape

- **Status banner.**
- **What it measures** — one paragraph, cited to the KRI (`kriId` + link).
- **What happened** — the numbers, the window, the shape, cited.
- **Likely drivers** — ranked, each with a citation and a confidence word (likely / possible / speculative).
- **What it doesn't mean** — the honest caveats.
- **Suggested follow-ups** — KRIs/tables a human might pull next.

## Discipline
Plain language over jargon. Every number carries its window and link. Label causal statements by confidence; prefer "coincides with" over "caused by" unless the mechanism is explicit in the data.
