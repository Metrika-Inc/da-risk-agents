---
name: board-pack-author
description: Render an assembled risk pack (from risk-pack) into a polished, review-ready document — a PowerPoint deck for a committee readout or a Word memo for the board book — preserving every Metrika citation and deep-link. Use after risk-pack has gathered and cited the content. Requires the environment's document-creation skills (pptx / docx).
---

# Author the board / committee pack

Turn the cited content from `risk-pack` into a document a human can present or drop into a board book — without losing a single reference.

## Choose the format
- **Committee readout / all-hands** → **PowerPoint** (`.pptx`). One idea per slide, chart-forward, speaker notes carry the detail + citations.
- **Board book / risk memo** → **Word** (`.docx`). Prose, tables, a formal evidence appendix.

Before creating either, **read the matching document-creation skill in this environment first** (`pptx` skill for decks, `docx` skill for memos) and follow it — it encodes the environment's rendering constraints. Do not hand-roll file XML.

## Non-negotiables when rendering
- **Citations survive the render.** Every risk claim keeps its `kriId`/object id and a clickable Metrika `webUrl` — as a footnote, a slide-note line, or an evidence-appendix row. A chart without its source link is not done.
- **Status banner on the cover** and in the document footer: DRAFT for {committee}; not a decision or advice; sign-off required. (From `review-gate`.)
- **Charts trace to data.** Any chart is built from Metrika timeseries you pulled; caption it with the KRI + window + link. Never draw a trend you didn't fetch.
- **Evidence appendix** — a final section listing every Metrika object id + deep-link used, so the pack is auditable on its own.

## Flow
1. Confirm the content from `risk-pack` is complete and cited.
2. Read the relevant `pptx` / `docx` skill.
3. Build the file: cover + banner → exec summary → posture by theme → incidents → watch items → evidence appendix.
4. Save to the outputs location and hand the reviewer the file plus a one-line summary of what needs their sign-off.

## Discipline
The document is a faithful rendering of cited content — authoring adds format, never facts. If a slide would state something the pack didn't evidence, cut it or send it back to `risk-pack` for sourcing.
