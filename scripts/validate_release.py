#!/usr/bin/env python3
"""Validate the local Goals release package without external dependencies."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

MARKETPLACES = (".agents/plugins/marketplace.json", ".claude-plugin/marketplace.json")
PLUGINS = ("plugins/goals/.codex-plugin/plugin.json", "plugins/goals/.claude-plugin/plugin.json")
LINK = re.compile(r"(?<!!)\]\(([^)]+)\)")


def validate_repository(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    manifests: dict[str, dict] = {}
    for name in (*MARKETPLACES, *PLUGINS):
        try:
            value = json.loads((root / name).read_text(encoding="utf-8"))
            if not isinstance(value, dict):
                raise ValueError("root must be an object")
            manifests[name] = value
        except (OSError, UnicodeError, ValueError) as error:
            errors.append(f"{name}: cannot read JSON object: {error}")
    if len(manifests) != 4:
        return errors

    codex_market, claude_market, codex_plugin, claude_plugin = (manifests[name] for name in (*MARKETPLACES, *PLUGINS))
    entries = []
    for name, market in zip(MARKETPLACES, (codex_market, claude_market)):
        if market.get("name") != "goals-marketplace":
            errors.append(f"{name}: name must be goals-marketplace")
        plugins = market.get("plugins")
        if not isinstance(plugins, list) or len(plugins) != 1 or not isinstance(plugins[0], dict):
            errors.append(f"{name}: plugins must contain exactly one object")
            return errors
        entries.append(plugins[0])

    codex_entry, claude_entry = entries
    for name, item in zip((*MARKETPLACES, *PLUGINS), (codex_entry, claude_entry, codex_plugin, claude_plugin)):
        if item.get("name") != "goals":
            errors.append(f"{name}: plugin name must be goals")
    versions = [claude_market.get("version"), claude_entry.get("version"), codex_plugin.get("version"), claude_plugin.get("version")]
    if not all(isinstance(v, str) and re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", v) for v in versions) or len(set(versions)) != 1:
        errors.append("marketplace and plugin version fields must be matching semantic versions")

    codex_source = codex_entry.get("source")
    if not isinstance(codex_source, dict) or codex_source.get("source") != "local" or codex_source.get("path") != "./plugins/goals":
        errors.append(f"{MARKETPLACES[0]}: source.path must point to ./plugins/goals as a local source")
    if claude_entry.get("source") != "./plugins/goals":
        errors.append(f"{MARKETPLACES[1]}: source must point to ./plugins/goals")
    if claude_entry.get("strict") is not True:
        errors.append(f"{MARKETPLACES[1]}: strict must be true")
    for name, plugin in zip(PLUGINS, (codex_plugin, claude_plugin)):
        if plugin.get("skills") != "./skills/":
            errors.append(f"{name}: skills must point to ./skills/")

    skill = root / "plugins/goals/skills/goals"
    required = (
        "SKILL.md", "agents/openai.yaml", "references/planning.md",
        "references/execution.md", "references/archive.md", "assets/index.md", "assets/goal.md",
    )
    for name in required:
        if not (skill / name).is_file():
            errors.append(f"{(skill / name).relative_to(root)}: required skill resource is missing")
    skills_root = skill.parent
    if not skills_root.is_dir() or {p.name for p in skills_root.iterdir() if p.is_dir()} != {"goals"}:
        errors.append("plugins/goals/skills: expected exactly the goals skill directory")

    skill_file = skill / "SKILL.md"
    if skill_file.is_file():
        content = skill_file.read_text(encoding="utf-8")
        if not re.match(r"\A---\nname: goals\ndescription: .+\n---\n", content):
            errors.append(f"{skill_file.relative_to(root)}: invalid name or description frontmatter")
    metadata = skill / "agents/openai.yaml"
    if metadata.is_file():
        text = metadata.read_text(encoding="utf-8")
        for field in ("interface:", "display_name:", "short_description:", "default_prompt:"):
            if field not in text:
                errors.append(f"{metadata.relative_to(root)}: missing {field}")
        if "$goals" not in text:
            errors.append(f"{metadata.relative_to(root)}: default prompt must mention $goals")

    if skill.is_dir():
        for file in skill.rglob("*.md"):
            for raw in LINK.findall(file.read_text(encoding="utf-8")):
                parsed = urlsplit(raw)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                target = (file.parent / unquote(parsed.path)).resolve()
                if not target.is_relative_to(skill.resolve()) or not target.is_file():
                    errors.append(f"{file.relative_to(root)}: missing or unsafe linked resource: {raw}")

    index = skill / "assets/index.md"
    goal = skill / "assets/goal.md"
    if index.is_file() and goal.is_file():
        index_text, goal_text = index.read_text(encoding="utf-8"), goal.read_text(encoding="utf-8")
        if not re.search(r"\[ \] \[G01[^]]*\]\(goal\.md\)", index_text):
            errors.append(f"{index.relative_to(root)}: sample queue must link to goal.md")
        for field in ("# G01", "Status: planned", "Prerequisites: None", "## Acceptance criteria", "## Verification"):
            if field not in goal_text:
                errors.append(f"{goal.relative_to(root)}: missing template field {field}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate_repository(args.root)
    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1
    print("Release validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
