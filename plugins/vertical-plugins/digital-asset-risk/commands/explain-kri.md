---
description: Explain a KRI or a KRI spike in plain language, with drivers corroborated from Metrika (read-only)
argument-hint: "[kri id | risk question] [entity]"
---

# /explain-kri

Make an indicator legible to a reviewer without overclaiming causation.

1. Load `review-gate`, `metrika-mcp`, `risk-evidence`, then `kri-explainer`.
2. If given a question rather than an id, pick the KRI(s) with `metrika_kri_find_smart` and carry the `why`.
3. Follow the `kri-explainer` skill: define it → show the movement (numbers + window) → corroborate likely drivers → bound the claim.
4. Label causal statements by confidence (likely / possible / speculative). Every number carries its window and Metrika deep-link.

Read-only.
