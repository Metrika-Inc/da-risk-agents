---
description: Draft a pre-onboarding due-diligence assessment for an asset/chain across the six risk dimensions (read-only; report writes gated)
argument-hint: "[asset] [chain] [--framework <template name>]"
---

# /onboarding-dd

Draft an evidenced pre-onboarding risk assessment for the **onboarding committee**. It does not approve onboarding.

1. Load `review-gate`, `metrika-mcp`, `risk-evidence`, then `onboarding-dd`.
2. Confirm coverage (`metrika_assets_and_chains`); pick the framework(s) via `metrika_report_templates_list` + `metrika_framework_questions_find`.
3. Work the six dimensions — peg, reserves, liquidity, chain health, concentration, sanctions — each cited to KRIs/datatables + deep-links.
4. Output the DD memo: proposed rating (labelled *proposed*), dimension findings, red flags/blockers, open items for the committee, evidence appendix.

Read-only by default. Staging the assessment as a Metrika report is a **gated write** — propose, get explicit human OK, create **draft** only. Never legal/investment advice.
