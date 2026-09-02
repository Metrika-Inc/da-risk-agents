# Metrika Digital Asset Risk — Claude Agent Templates

Three Claude agent templates for digital-asset **risk & compliance**, wired to the **Metrika MCP server** as the live data layer (KRIs, monitors/incidents, and report frameworks across Metrika's covered chains and assets).

Modeled on the [`anthropics/financial-services`](https://github.com/anthropics/financial-services) plugin pattern: role-named **agent plugins** on top of a shared **vertical plugin** (skills + slash commands + the MCP connector). Installable as **Claude Cowork** plugins.

> [!IMPORTANT]
> Nothing here constitutes investment, legal, tax, or accounting advice. These agents **draft analyst work product** — briefings, triage notes, due-diligence memos, board packs — for review by a qualified professional. They **do not** make investment recommendations, execute transactions, bind risk, approve onboarding, or change monitors. Every output is staged for human sign-off. Every risk claim is cited to a **Metrika KRI id / deep-link** for auditability. You are responsible for verifying outputs and for compliance with the laws and regulations that apply to your firm.

This is a **Level 2–3 autonomy** system: AI co-pilot / human-supervised. Not autonomous execution. See [`docs/AUTONOMY.md`](docs/AUTONOMY.md) and [`docs/GUARDRAILS.md`](docs/GUARDRAILS.md).

## The three agents

| Agent | Plugin | What it drafts |
|---|---|---|
| **Digital Asset Risk Controller** | [`risk-controller`](plugins/agent-plugins/risk-controller) | Morning risk briefings · incident triage · KRI-spike explanations · escalation memos |
| **Token/Asset Onboarding Due Diligence** | [`asset-onboarding-dd`](plugins/agent-plugins/asset-onboarding-dd) | Pre-onboarding assessments (peg · reserves · liquidity · chain health · concentration · sanctions) on Metrika DD frameworks → committee memo |
| **Risk Reporting & Governance Analyst** | [`risk-reporting`](plugins/agent-plugins/risk-reporting) | Board / risk-committee packs from KRI trends + incident history, rendered to pptx/docx |

Each agent plugin is **self-contained** — it bundles the skills it uses (synced from the vertical plugin), so installing the agent is all you need.

## Repository layout

```
metrika-digital-asset-risk/
├── .claude-plugin/marketplace.json        # registers the vertical + 3 agent plugins
├── plugins/
│   ├── vertical-plugins/
│   │   └── digital-asset-risk/            # SHARED — the single source of truth
│   │       ├── .claude-plugin/plugin.json
│   │       ├── .mcp.json                  # Metrika MCP connector (https://mcp.metrika.co/mcp)
│   │       ├── commands/                  # /morning-brief /triage /explain-kri /escalation-memo /onboarding-dd /board-pack
│   │       └── skills/                    # 3 guardrail skills + 7 workflow skills
│   └── agent-plugins/
│       ├── risk-controller/               # agents/<slug>.md + bundled skills
│       ├── asset-onboarding-dd/
│       └── risk-reporting/
├── scripts/
│   ├── sync-agent-skills.py               # propagate skills: vertical → agent bundles
│   └── check.py                           # lint manifests, frontmatter, skill drift, MCP config
└── docs/                                  # GUARDRAILS · AUTONOMY · sample-output specs · blog draft
```

**Edit skills only in `plugins/vertical-plugins/digital-asset-risk/skills/`**, then run `python3 scripts/sync-agent-skills.py` to propagate them into the agent bundles. `python3 scripts/check.py` fails if a bundle has drifted.

## Shared skills

| Skill | Role |
|---|---|
| `review-gate` | **Guardrail floor** — draft-only, human-in-the-loop, no advice, read-only by default, mutation gate |
| `metrika-mcp` | How to drive the Metrika MCP correctly (validate entities, opaque ids, read vs mutation, deep-links) |
| `risk-evidence` | **Guardrail floor** — every risk claim carries its KRI id + Metrika deep-link |
| `morning-brief` · `incident-triage` · `kri-explainer` · `escalation-memo` | Risk Controller workflows |
| `onboarding-dd` | Six-dimension due diligence on Metrika DD frameworks |
| `risk-pack` · `board-pack-author` | Governance-pack assembly + docx/pptx rendering |

All three agents bundle the guardrail floor (`review-gate`, `metrika-mcp`, `risk-evidence`); `check.py` enforces it.

## How it maps to Metrika

Read-only tools do the work; three mutation tools are gated behind explicit human authorization.

- **Risk Controller** → `kri_monitor_alert_stats` / `_incidents`, `kri_monitors_find` / `_get`, `kri_monitor_threshold_audit`, `kri_find_smart` / `kri_get_timeseries`, `adverse_media_*`, on-chain `datatable_*`.
- **Onboarding DD** → `report_templates_list` + `framework_questions_find` (structure), then `kri_find_smart` / `datatable_*` across the six dimensions; report writes (`report_create` / `report_generate_from_template` / `report_update_answer`) are **gated, draft-only**.
- **Risk Reporting** → `*_alert_stats` (period + PoP), `kri_get_timeseries` (trends), concentration / chain-health / sanctions `datatable_*`; renders via the environment's `pptx` / `docx` skills.

## Install

### Cowork
Settings → **Plugins → Add plugin**, then either paste this repo's URL and pick plugins from the marketplace list, or upload a zip of any directory under `plugins/`. Install `digital-asset-risk` (shared) first, then the agents you want.

### Claude Code
```bash
claude plugin marketplace add <this-repo-url>
claude plugin install digital-asset-risk@metrika-digital-asset-risk   # shared skills + Metrika connector, first
claude plugin install risk-controller@metrika-digital-asset-risk
claude plugin install asset-onboarding-dd@metrika-digital-asset-risk
claude plugin install risk-reporting@metrika-digital-asset-risk
```
Authenticate the Metrika MCP server when prompted. Then: agents appear in Cowork dispatch, and the slash commands (`/morning-brief`, `/triage`, `/explain-kri`, `/escalation-memo`, `/onboarding-dd`, `/board-pack`) are available in-session.

## Sample tasks
See [`docs/sample-outputs/README.md`](docs/sample-outputs/README.md) for the runnable sample tasks used in the demo (each read-only, each producing a cited draft).
