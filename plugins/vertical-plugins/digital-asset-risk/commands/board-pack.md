---
description: Draft a board / risk-committee risk pack from KRI trends and incident history, rendered to docx/pptx (read-only)
argument-hint: "[entity | portfolio] [--period <e.g. Q2-2026>] [--format pptx|docx]"
---

# /board-pack

Assemble and render a **draft** governance risk pack for a committee.

1. Load `review-gate`, `metrika-mcp`, `risk-evidence`, then `risk-pack`, then `board-pack-author`.
2. Gather + cite content with `risk-pack`: incident history (PoP), KRI trends, structural snapshot; lead every section with what changed.
3. Read the environment's `pptx`/`docx` skill, then render with `board-pack-author`, preserving every citation + deep-link and the DRAFT banner on cover and footer.
4. Deliver the file plus a one-line summary of what needs committee sign-off.

Read-only. The pack is a draft input to governance decisions, not a decision or advice.
