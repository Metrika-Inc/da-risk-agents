# Sample tasks (for the live demo)

Each task below is **read-only** and produces a **cited draft**. They double as the all-hands demo script and as acceptance checks. Run each against live Metrika data and drop the resulting draft (redacted as needed) alongside this file.

> All entities must be validated against `metrika_assets_and_chains` first. Use whatever assets/chains your org's Metrika credentials actually cover.

## 1. Risk Controller — morning brief
**Command:** `/morning-brief <watchlist> 24h`
**Expect:** worst-first snapshot; a "fired overnight" table (entity · monitor · severity · breaching value vs threshold · link); movers with numbers + windows; adverse-media headlines; a "for the reviewer" shortlist; DRAFT banner. Every line links to a KRI/incident in Metrika.
**Check:** no uncited claim; nothing executed; coverage gaps named, not silently treated as "fine."

## 2. Risk Controller — triage → escalation memo
**Command:** `/triage <recent critical/high incident id>` then `/escalation-memo`
**Expect:** breach quantified vs threshold; corroboration (related KRIs / on-chain / adverse media); a signal-vs-noise read from `threshold_audit`; a *proposed* severity + next step; then a one-page memo with options (not instructions), blank owner/sender, and an evidence appendix.
**Check:** fact vs interpretation clearly separated; nothing sent or escalated.

## 3. Risk Controller — explain a spike
**Command:** `/explain-kri "why did <metric> move on <entity>?"`
**Expect:** what the KRI measures (cited), the movement with numbers + window, ranked candidate drivers each confidence-labelled and cited, honest "what it doesn't mean."
**Check:** no unbounded causal claims; "coincides with" over "caused by" unless mechanism is explicit.

## 4. Onboarding DD — assessment
**Command:** `/onboarding-dd <asset> <chain> --framework "Due Diligence Template"`
**Expect:** framework-structured memo across peg, reserves, liquidity, chain health, concentration, sanctions; each finding cited to KRIs/datatables; a *proposed* rating; red flags/blockers; open items for the committee; evidence appendix (incl. template `_id`).
**Check:** rating labelled a proposal; report-write **not** performed unless you explicitly authorize it in-session (and then only as a draft); absence-of-flag not treated as approval.

## 5. Risk Reporting — board pack
**Command:** `/board-pack <portfolio> --period <e.g. Q2-2026> --format pptx`
**Expect:** a rendered deck: cover + DRAFT banner, exec summary, posture by theme (charts from pulled timeseries, captioned with KRI + window + link), incident summary with PoP delta, movers/watch items, evidence appendix.
**Check:** every chart traces to data you fetched; citations survive into the file; DRAFT banner on cover and footer.


