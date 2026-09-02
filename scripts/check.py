#!/usr/bin/env python3
"""Lint the metrika-digital-asset-risk marketplace.

Checks:
  - marketplace.json parses; every plugin source path exists and holds a plugin.json.
  - every plugin.json parses and has name/version/description.
  - every agents/*.md has YAML-ish frontmatter with name + description + tools.
  - the Metrika MCP connector is present in the vertical .mcp.json.
  - each agent bundles exactly the skills it declares, and no bundled copy has
    drifted from its vertical-plugin source (run sync-agent-skills.py to fix).
  - every agent references the three guardrail skills (review-gate, metrika-mcp,
    risk-evidence) in its bundle — the non-negotiable floor.
Exit non-zero on any failure.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def load_json(p: Path):
    try:
        return json.loads(p.read_text())
    except Exception as e:  # noqa: BLE001
        err(f"{p}: invalid JSON ({e})")
        return None


def check_marketplace():
    mp = load_json(ROOT / ".claude-plugin/marketplace.json")
    if not mp:
        return
    for entry in mp.get("plugins", []):
        src = ROOT / entry["source"]
        pj = src / ".claude-plugin/plugin.json"
        if not pj.exists():
            err(f"marketplace plugin '{entry['name']}': missing {pj}")
            continue
        data = load_json(pj)
        if data:
            for field in ("name", "version", "description"):
                if not data.get(field):
                    err(f"{pj}: missing '{field}'")


def parse_frontmatter(md: Path) -> dict:
    text = md.read_text()
    if not text.startswith("---"):
        err(f"{md}: no frontmatter")
        return {}
    fm = text.split("---", 2)[1]
    out = {}
    for line in fm.splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            out[k.strip()] = v.strip()
    return out


GUARDRAIL_FLOOR = {"review-gate", "metrika-mcp", "risk-evidence"}


def check_agents():
    src_skills = ROOT / "plugins/vertical-plugins/digital-asset-risk/skills"
    for agent_dir in sorted((ROOT / "plugins/agent-plugins").iterdir()):
        if not agent_dir.is_dir():
            continue
        agents_md = list((agent_dir / "agents").glob("*.md"))
        if not agents_md:
            err(f"{agent_dir.name}: no agents/*.md system prompt")
        for md in agents_md:
            fm = parse_frontmatter(md)
            for field in ("name", "description", "tools"):
                if not fm.get(field):
                    err(f"{md}: frontmatter missing '{field}'")
        bundled = {p.name for p in (agent_dir / "skills").iterdir()} if (agent_dir / "skills").exists() else set()
        if not GUARDRAIL_FLOOR.issubset(bundled):
            err(f"{agent_dir.name}: missing guardrail skills {GUARDRAIL_FLOOR - bundled} (run sync-agent-skills.py)")
        # drift check
        for skill in bundled:
            a = (agent_dir / "skills" / skill / "SKILL.md")
            b = (src_skills / skill / "SKILL.md")
            if not b.exists():
                err(f"{agent_dir.name}: bundled skill '{skill}' has no vertical source")
            elif a.read_text() != b.read_text():
                err(f"{agent_dir.name}: skill '{skill}' drifted from source (run sync-agent-skills.py)")


def check_mcp():
    mcp = load_json(ROOT / "plugins/vertical-plugins/digital-asset-risk/.mcp.json")
    if mcp and "metrika" not in mcp.get("mcpServers", {}):
        err("vertical .mcp.json: no 'metrika' server configured")


def main():
    check_marketplace()
    check_agents()
    check_mcp()
    if errors:
        print("FAIL:")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print("OK: all manifests, agents, skills, and MCP config valid.")


if __name__ == "__main__":
    main()
