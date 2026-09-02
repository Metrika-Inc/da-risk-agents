---
description: Draft a morning digital-asset risk briefing for an entity or watchlist (read-only)
argument-hint: "[asset/chain or watchlist] [lookback, default 24h]"
---

# /morning-brief

Assemble a fully-cited overnight risk briefing as a **draft for the on-desk reviewer**.

1. Load `review-gate`, `metrika-mcp`, `risk-evidence`, then `morning-brief`.
2. Validate the entity/watchlist via `metrika_assets_and_chains`. If none given, ask which watchlist (or offer to run the standard desk watchlist).
3. Follow the `morning-brief` skill: what fired → what's open → what moved → adverse media.
4. Output worst-first, every line cited to a `kriId`/incident id + Metrika deep-link, opened with the DRAFT status banner.

Read-only. No monitor or threshold changes; no escalations executed.
