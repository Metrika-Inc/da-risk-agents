# Metrika Digital Asset Risk — plugins

Claude Cowork plugins for digital-asset risk & compliance, on the Metrika MCP data layer.
Three role-named agent plugins over one shared vertical plugin. Draft work product only,
Level 2-3 (human-supervised). Every risk claim cites a Metrika KRI id / deep-link.

## Structure
- `plugins/vertical-plugins/digital-asset-risk/` — SINGLE SOURCE OF TRUTH: skills/, commands/, .mcp.json
- `plugins/agent-plugins/<slug>/` — agents/<slug>.md system prompt + bundled skill copies

## Development workflow
1. Edit skills/commands ONLY in the vertical plugin.
2. `python3 scripts/sync-agent-skills.py` — propagate skills into agent bundles.
3. `python3 scripts/check.py` — lint manifests, agent frontmatter, MCP config, and skill drift. Must pass before commit.

## Non-negotiables (encoded in review-gate + risk-evidence, bundled by every agent)
- Draft only; never an executed action, binding decision, or investment/legal/tax advice.
- Read-only against Metrika by default; report writes are gated behind explicit human authorization and are draft-only (never status: complete).
- Every risk claim carries its Metrika object id + deep-link. No reference, no claim.

## Key files
- `.claude-plugin/marketplace.json` — registers all plugins
- `plugins/*/.claude-plugin/plugin.json` — plugin metadata (version gates update delivery)
- `agents/<slug>.md` — canonical system prompt
- `skills/*/SKILL.md` — auto-invoked knowledge/workflows
- `commands/*.md` — slash commands (/plugin:command)
