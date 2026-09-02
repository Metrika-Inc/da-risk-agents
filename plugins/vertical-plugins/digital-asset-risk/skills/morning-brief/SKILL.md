---
name: morning-brief
description: Assemble a morning digital-asset risk briefing for a watchlist or a single entity — what fired overnight, which KRIs moved, what's newly elevated, and what the reviewer should look at first. Read-only. Use for daily standup / start-of-day risk review. Requires metrika-mcp, risk-evidence, review-gate.
---

# Morning risk briefing

A tight, skimmable, fully-cited snapshot of overnight risk for a named entity or watchlist. Draft for the on-desk risk reviewer.

## Inputs
Entity or watchlist (assets/chains), and the lookback (default: since the previous briefing / last 24h). Validate every entity via `metrika_assets_and_chains`.

## Workflow

1. **What fired.** `metrika_kri_monitor_alert_stats` (KRI) and `metrika_adverse_media_monitor_alert_stats` (adverse media) over the window, grouped by entity/severity. Pull the noisiest monitors and any `critical`/`high`.
2. **What's open.** `metrika_kri_monitors_find` with `status: firing` for current breaches; `metrika_kri_monitor_incidents` for the overnight timeline where detail is warranted.
3. **What moved.** For each watched entity, `metrika_kri_find_smart` on the day's theme (peg, liquidity, bridging, concentration, chain health), then `metrika_kri_get_timeseries` on the few that matter; flag `last` vs `p90`/`p50`.
4. **News.** `metrika_adverse_media_monitor_incidents` for the window; summarize headlines by risk category, link sources.

## Output shape

- **Status banner** (from `review-gate`).
- **Top of mind** — 3–6 bullets, worst first, each cited (`kriId`/incident id + `webUrl`).
- **Fired overnight** — table: entity · monitor · severity · breaching value vs threshold · link.
- **Movers** — KRIs whose `last` diverges from recent distribution, with the number, window, and link.
- **Adverse media** — headline · category · severity · source link.
- **For the reviewer** — the 1–3 items most worth a human look, framed as questions, not directives.
- **Quiet** — one line naming what was checked and clear, so silence is evidenced, not assumed.

## Discipline
Worst-first, not exhaustive. Every line cited. "Elevated" always carries a number, a window, and a link. Movement ≠ breach — say which it is. If a watched entity has no data, list it as a coverage gap, not as "fine."
