---
name: metrika-mcp
description: How to drive the Metrika MCP server correctly — the single data layer for every digital-asset-risk agent. Covers validating assets/chains before querying, treating KRI/table/report ids as opaque handles, the read-only vs mutation tool split, and always surfacing the platform deep-link (webUrl). Load this before any Metrika call.
---

# Using the Metrika MCP

Metrika is the **only** source of risk facts for these agents. Every risk claim traces back to a Metrika object. Do not substitute general knowledge, training data, or web results for a Metrika metric.

## Always validate the entity first

Before any `asset`/`chain` filter, call `metrika_assets_and_chains` once and pick the **exact** canonical identifier from `assetIdentifiers` / `chainIdentifiers`. Do not guess spellings (Metrika uses `POL`, not `MATIC`; `base` shares `ETH`). If the user's asset/chain has no match, say it is not covered — do not query with an unmatched value.

Metrika covers **chains and assets, not DeFi protocols**. "Aave TVL on Ethereum" is not modeled; an `AAVE` token may be.

## IDs are opaque handles

`kriId`, `tableId`, report `_id`, `monitorId` — pass through **verbatim**. Never parse, split, reformat, or reconstruct them. Get them from the matching `*_find` / `*_list` tool; never invent one.

## Read-only vs mutation (critical)

**Read-only — safe, this is where the agents live:**
`metrika_assets_and_chains`, `metrika_kri_find`, `metrika_kri_find_smart`, `metrika_kri_get_timeseries`, `metrika_kri_monitors_find`, `metrika_kri_monitor_get`, `metrika_kri_monitor_incidents`, `metrika_kri_monitor_alert_stats`, `metrika_kri_monitor_threshold_audit`, `metrika_adverse_media_monitors_find`, `metrika_adverse_media_monitor_get`, `metrika_adverse_media_monitor_incidents`, `metrika_adverse_media_monitor_alert_stats`, `metrika_datatable_find`, `metrika_datatable_get`, `metrika_report_templates_list`, `metrika_framework_questions_find`, `metrika_reports_find`, `metrika_report_get`.

**Mutations — WRITE to the org and/or trigger billable AI jobs. Gated by `review-gate`:**
`metrika_report_create`, `metrika_report_generate_from_template`, `metrika_report_update_answer`.

Never call a mutation tool without explicit, in-session human authorization, and never write a report answer with `status: complete`. See the `review-gate` skill.

## Choosing KRI tools

- Natural-language risk question ("is the peg healthy?") → `metrika_kri_find_smart` (AI-ranked shortlist with a `why` per KRI).
- "Every KRI for asset X / chain Y" → `metrika_kri_find` (full catalog, you filter).
- Have a `kriId`, want history → `metrika_kri_get_timeseries` (returns `timeseriesStats`: min/max/mean/p50/p90/p95/last).

## Aggregate before you dump

For alert history, call the `*_alert_stats` tools first (counts, noisiest monitors) before pulling raw `*_incidents`. Don't flood a brief with raw incident rows.

## Always surface the deep-link

Every Metrika object comes back with a `webUrl`. Render it verbatim as a clickable markdown link whenever you cite the object — proactively. Never build a URL yourself. These links are the auditor's path back to source (see `risk-evidence`).

## Values are raw

Percentages are usually 0–1 fractions (`balance_per: 0.3223` = 32.23%); timestamps are ISO UTC; `point` may be `null` for real gaps. State units; don't invent precision.
