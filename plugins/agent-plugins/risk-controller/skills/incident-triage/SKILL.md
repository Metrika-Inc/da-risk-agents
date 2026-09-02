---
name: incident-triage
description: Triage a firing Metrika incident (or a cluster) into a draft assessment — what breached, how far past threshold, corroborating KRIs and on-chain data, likely nature (real signal vs known-noisy monitor), and a proposed severity and next step for a human to action. Read-only. Requires metrika-mcp, risk-evidence, review-gate.
---

# Incident triage

Turn an alert into a decision-ready draft. You classify and recommend; the reviewer actions.

## Inputs
An incident id, a monitor name, or an entity + window. Resolve with `metrika_kri_monitor_incidents` / `metrika_adverse_media_monitor_incidents`.

## Workflow

1. **Anchor the incident.** Get the incident: `openedAt`, status, derived severity, and the `transitions[]` — the breaching rule, condition, threshold, and the value that tripped it. Get the monitor config (`metrika_kri_monitor_get`) for the full rule set.
2. **Quantify the breach.** How far past threshold? Pull the KRI timeseries around `openedAt` (`metrika_kri_get_timeseries`, window aligned to the incident) — is this a spike, a step-change, or a drift over the line?
3. **Signal vs noise.** `metrika_kri_monitor_threshold_audit` on this monitor over a trailing window: how often does it fire, and where does the trigger value sit vs the distribution (`p90`/`p95`)? A monitor that fires constantly and trips near its own p50 is likely noisy — say so, with the numbers.
4. **Corroborate.** Look for independent confirmation: related KRIs (`kri_find_smart`), on-chain datatables (large transfers, holder/sanctions shifts, governance/admin events), and adverse-media incidents on the same entity in the same window. Convergence raises confidence; isolation lowers it.
5. **Draft the assessment.**

## Output shape

- **Status banner.**
- **Incident** — entity, monitor, opened, breaching rule + value vs threshold, link.
- **How far past** — the number and the trend shape, cited.
- **Corroboration** — what agrees / disagrees, each cited; net read on confidence.
- **Noise check** — this monitor's firing rate + trigger-value percentiles, cited.
- **Proposed severity & next step** — clearly labelled *proposed*: e.g. "escalate to {role}", "watch", "candidate false positive — consider threshold review." Never executed.
- **Open questions** — what a human should verify before acting.

## Discipline
Separate the breach (fact) from your read of it (interpretation). Do not downgrade a corroborated critical because a monitor is usually noisy — flag the tension and leave the call to the reviewer.
