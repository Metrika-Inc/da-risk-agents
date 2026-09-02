---
name: risk-pack
description: Assemble a board / risk-committee risk pack from Metrika KRI trends and incident history over a reporting period — portfolio risk posture, what changed, incident summary, notable movers, and watch items. Produces a review-ready draft pack (content + structure). Read-only. Pair with board-pack-author to render docx/pptx. Requires metrika-mcp, risk-evidence, review-gate.
---

# Risk reporting pack (draft)

A period-over-period risk narrative for a governance audience, grounded in Metrika. You draft the pack; the committee owns the conclusions.

## Inputs
Scope (entity / portfolio / watchlist), reporting period (e.g. the quarter), and the prior period for comparison. Validate entities via `metrika_assets_and_chains`.

## Workflow

1. **Incident history.** `metrika_kri_monitor_alert_stats` and `metrika_adverse_media_monitor_alert_stats` over the period (and the prior period). Counts by entity / severity / risk category; noisiest monitors; period-over-period delta. Drill into `critical`/`high` with the incident tools only where the pack needs the story.
2. **KRI trends.** For each scope entity and risk theme, select the handful of KRIs that carry the story (`kri_find_smart`), pull `metrika_kri_get_timeseries` across the period, and report trend + end value vs distribution. Prefer a small set of decision-relevant indicators over a data dump.
3. **Structural risk snapshot.** Point-in-time concentration / chain-health datatables where governance cares (top-holder share, validator concentration, SDN exposure).
4. **Change is the headline.** The committee wants *what moved and why it matters*, not a metrics catalogue. Lead every section with the change.
5. **(Optional) frameworks.** If the committee maps to an RMF, pull the relevant framework via `metrika_framework_questions_find` (e.g. GBBC / SCB / Network Risk Assessment) and align sections to it.

## Pack structure
- **Cover & status banner** — period, scope, "DRAFT for {committee} review."
- **Executive summary** — 5–7 bullets: overall posture, biggest changes, top risks, cited.
- **Risk posture by theme / entity** — trend charts/tables, each cited.
- **Incident summary** — period totals, severity mix, PoP delta, notable incidents with links.
- **Movers & watch items** — what deteriorated / improved; what to watch next period.
- **Appendix** — full evidence list (object ids + deep-links); methodology & data caveats.

## Discipline
Governance-grade means conservative and cited: no unreferenced claim, PoP comparisons on a like-for-like window, and explicit data-quality caveats (coverage gaps, monitor changes mid-period). Facts from Metrika; the risk opinion is the committee's — present analysis as input, labelled as such. Hand off to `board-pack-author` for the rendered document.
