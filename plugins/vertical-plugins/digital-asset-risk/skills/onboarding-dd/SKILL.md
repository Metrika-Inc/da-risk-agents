---
name: onboarding-dd
description: Build a pre-onboarding risk assessment for a token/asset (or a chain) across peg, reserves/backing, liquidity, chain health, concentration, and sanctions exposure — evidenced from Metrika KRIs, datatables, and report frameworks. Produces a draft recommendation memo for the onboarding committee. Does not approve onboarding. Report writes are gated. Requires metrika-mcp, risk-evidence, review-gate.
---

# Pre-onboarding due diligence (draft)

A structured, evidenced first-pass risk assessment to help a human onboarding committee decide. You assemble and recommend; the committee approves or rejects.

## Step 0 — Coverage & framework
1. `metrika_assets_and_chains` — confirm the asset/chain is covered; get canonical ids. If not covered, stop and report the gap (an un-onboardable-via-Metrika finding is itself a finding).
2. `metrika_report_templates_list` — pick the framework(s) that fit the mandate. Onboarding-relevant templates seen in the org include: **Due Diligence Template**, **Due Diligence Report**, **BNY Stablecoin DD**, **BBVA Group Crypto Asset Admission**, **SEC_Stablecoin_example**, **DTCC L1/L2 Due Diligence**, **VARA Asset / VARA Network Template**, **Basel Classification**, **MICAR Network Reporting**. Use `metrika_framework_questions_find` to read the actual questions the committee expects answered, and structure the assessment around them.

## The six risk dimensions → Metrika evidence
For each, use `metrika_kri_find_smart` (question-led) then `metrika_kri_get_timeseries`, plus the datatables noted:

| Dimension | Look for | Metrika sources |
|---|---|---|
| **Peg stability** | deviation, depth, depeg events | peg/price KRIs; `exchange_markets` (price, spread, depeg %) |
| **Reserves / backing** | what backs it, quality, maturity | `fund_holdings`; backing/attestation KRIs; the DD template's reserve questions |
| **Liquidity** | venues, volume, spread, exit capacity | `exchange_markets`; liquidity/volume KRIs |
| **Chain health** | validator/node/client concentration, performance, upgrades | `validator_centralization`, `node_centralization`, `validator_performance`, `source_code_activity`, `network_performance`, `network_upgrades` |
| **Concentration** | holder centralization, whales, admin/governance power | `token_holders`, `holder_distribution`, `governance_voting_power`, `governance_events` (admin keys, upgradeability) |
| **Sanctions / illicit** | SDN holders, exposure, negative news | `sanctioned_holders`, `sanctions_list_updates`; `metrika_adverse_media_monitor_incidents` |

## Step N — the mutation gate (report writing)
If the committee wants the assessment staged as a Metrika report from a template: **do not** call `metrika_report_generate_from_template` / `report_create` on your own. Propose it (template, entity, title), note it is a real write + billable AI jobs, wait for explicit human "yes," and create only a **draft** — never mark answers `complete`. See `review-gate`.

## Output shape (the DD memo)
- **Status banner** — draft for the onboarding committee; not an approval; not legal/investment advice.
- **Summary** — asset/chain, proposed use, and a **proposed** risk rating (labelled proposed), with the 3–5 findings that drive it.
- **Dimension-by-dimension** — for each of the six: finding, the evidence (cited `kriId`/table + `webUrl`), and residual uncertainty.
- **Red flags & blockers** — anything that should stop or condition onboarding (e.g. SDN holders present, single-entity control of upgrade keys).
- **Open items for the committee** — what Metrika can't answer (legal opinions, issuer contracts, off-chain reserves attestations) and must be sourced elsewhere.
- **Evidence appendix** — every object id + link; the framework template `_id`(s) used.

## Discipline
Absence of a red flag is not a green light — say what you checked and what you couldn't. Chain-level risk (e.g. validator concentration) still applies to an asset deployed on that chain. The rating is an input to a human decision, never the decision.
