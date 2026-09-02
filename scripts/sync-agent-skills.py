#!/usr/bin/env python3
"""Sync shared skills from the vertical plugin into each agent plugin bundle.

Single source of truth: plugins/vertical-plugins/digital-asset-risk/skills/
Agent plugins are self-contained, so each bundles copies of the skills it uses.
Edit skills ONLY in the vertical plugin, then run this to propagate.
"""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "plugins/vertical-plugins/digital-asset-risk/skills"
AGENTS = ROOT / "plugins/agent-plugins"

# Which shared skills each agent bundles (mirrors each agent's "Skills this agent uses").
AGENT_SKILLS = {
    "risk-controller": [
        "review-gate", "metrika-mcp", "risk-evidence",
        "morning-brief", "incident-triage", "kri-explainer", "escalation-memo",
    ],
    "asset-onboarding-dd": [
        "review-gate", "metrika-mcp", "risk-evidence", "onboarding-dd",
    ],
    "risk-reporting": [
        "review-gate", "metrika-mcp", "risk-evidence", "risk-pack", "board-pack-author",
    ],
}


def main() -> None:
    for agent, skills in AGENT_SKILLS.items():
        dest_root = AGENTS / agent / "skills"
        if dest_root.exists():
            shutil.rmtree(dest_root)
        dest_root.mkdir(parents=True, exist_ok=True)
        for skill in skills:
            src = SRC / skill
            if not src.exists():
                raise SystemExit(f"ERROR: {agent} declares missing skill '{skill}' ({src})")
            shutil.copytree(src, dest_root / skill)
        print(f"synced {len(skills):>2} skills -> {agent}")
    print("done.")


if __name__ == "__main__":
    main()
