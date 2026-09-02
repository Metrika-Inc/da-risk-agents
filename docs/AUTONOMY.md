# Autonomy level

These agents are deliberately **Level 2–3: AI co-pilot / human-supervised.** Not autonomous execution.

A rough ladder, and where these sit:

| Level | Description | This system |
|---|---|---|
| 0 | Manual — human does everything | — |
| 1 | Assistive — AI suggests, human does all the work | — |
| **2** | **Co-pilot — AI drafts the work product; human reviews and edits every output** | **← default** |
| **3** | **Supervised — AI runs a workflow end-to-end; human authorizes any state change and signs off the result** | **← onboarding DD report staging, under the mutation gate** |
| 4 | Conditional autonomy — AI executes within limits, human on exceptions | not permitted |
| 5 | Full autonomy — AI executes without human in the loop | not permitted |

## What that means in practice

- The agents **read** freely from Metrika and **produce drafts**. That is Level 2 and covers almost everything the three agents do: briefings, triage, explanations, memos, assessments, packs.
- The single place a state change can happen — staging a due-diligence report in Metrika — is Level 3: the human explicitly authorizes it in-session, and the result is a **draft**, never marked complete. The human completes and owns it in the platform.
- No agent operates at Level 4+. There is no path in these templates by which Claude approves onboarding, escalates a live incident, changes a monitor, or sends anything.

## Why draw the line here

Digital-asset risk decisions carry regulatory, financial, and legal weight, and the humans in the loop are accountable for them. The value of the agent is **speed and coverage on the drafting and evidence-gathering** — the parts that are slow and citation-heavy — while the **judgement and the action stay with the qualified reviewer.** Keeping every output cited and clearly a draft is what makes that division safe and auditable.

## Raising autonomy later (out of scope for the prototype)

If the firm later wants more autonomy for a narrow, well-understood task, it should come with: explicit written scope, hard tool-level restrictions (not just prompt guardrails), logging of every action, a reversible/draft-first design, and a named accountable owner — introduced one task at a time, never as a blanket setting.
