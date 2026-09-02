---
description: Triage a firing Metrika incident (or cluster) into a draft assessment (read-only)
argument-hint: "[incident id | monitor name | entity + window]"
---

# /triage

Turn an alert into a decision-ready **draft** assessment. You classify and recommend; a human actions.

1. Load `review-gate`, `metrika-mcp`, `risk-evidence`, then `incident-triage`.
2. Resolve the incident(s) via `metrika_kri_monitor_incidents` / `metrika_adverse_media_monitor_incidents`.
3. Follow the `incident-triage` skill: anchor the breach → quantify → signal-vs-noise (`threshold_audit`) → corroborate → draft.
4. Output the breach (fact) separately from your read (interpretation); propose a severity/next step, labelled *proposed*; list open questions. Every claim cited.

Read-only. Severity and next steps are proposals for a human, never executed.
