#!/usr/bin/env python3
"""Create disposable, deterministic repositories for the behavioral cases."""
import argparse
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parent
LEGACY = ROOT.parent / "tests" / "fixtures" / "legacy-queue"

INDEX = """# Example goals

## Operating Rules

Work eligible goals in queue order. Preserve unrelated edits. Commit only when requested.

## Verification

Run each goal's verification command.

## Queue

{queue}
"""
GOAL = """# {id} - {title}

Status: {status}

Prerequisites: {deps}

## Objective

{objective}

## Source / context

Example project request.

## Scope

{objective}

## Non-goals

Other goals and unrelated files.

## Acceptance criteria

{acceptance}

## Definition of done

Acceptance criteria and verification pass. Record the result and update the index.

## Verification

{verify}
"""

def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

def git(root, *args):
    subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True)

def create_queue(root, rows):
    queue = []
    for goal_id, title, status, deps, objective, acceptance, verify in rows:
        filename = goal_id.lower() + ".md"
        queue.append(f"- [{'x' if status == 'complete' else ' '}] [{goal_id} - {title}]({filename})")
        write(root / "goals" / filename, GOAL.format(
            id=goal_id, title=title, status=status, deps=deps, objective=objective,
            acceptance=acceptance, verify=verify))
    write(root / "goals" / "index.md", INDEX.format(queue="\n".join(queue)))

def row(goal_id, title, status, deps, target, text):
    return (goal_id, title, status, deps, f"Create {target} containing {text} on one line.",
            f"{target} contains exactly {text} followed by a newline.",
            f"`python3 -c \"from pathlib import Path; assert Path('{target}').read_text() == '{text}\\n'\"`")

def materialize(root, scenario):
    root.mkdir(parents=True)
    if scenario in ("legacy-dirty", "archive"):
        shutil.copytree(LEGACY, root, dirs_exist_ok=True)
        # Avoid requiring a commit in these tests. The legacy rules are preserved in G01.
        index = root / "goals/index.md"
        data = index.read_text(encoding="utf-8")
        data = data.replace("Complete one goal per commit and finish the previous goal's commit before starting another.", "Commit only when requested.")
        index.write_text(data, encoding="utf-8")
    elif scenario in ("queue", "failure", "interrupted"):
        if scenario == "queue":
            rows = [
                row("G01", "First", "planned", "None", "first.txt", "first"),
                row("G02", "Blocked", "blocked", "None", "blocked.txt", "blocked"),
                row("G03", "Dependent", "planned", "G02", "dependent.txt", "dependent"),
                row("G04", "Independent", "planned", "None", "independent.txt", "independent"),
                row("G05", "Missing", "planned", "G99", "missing.txt", "missing"),
                row("G06", "Cycle one", "planned", "G07", "cycle1.txt", "cycle1"),
                row("G07", "Cycle two", "planned", "G06", "cycle2.txt", "cycle2"),
            ]
            create_queue(root, rows)
            with (root / "goals/g02.md").open("a", encoding="utf-8") as file:
                file.write("\n## Blocked notes\n\n- Blocker: wording is undecided.\n- Tried: reviewed the request.\n- Needed from user: wording.\n")
        elif scenario == "failure":
            r = list(row("G01", "Unverifiable", "planned", "None", "result.txt", "ready"))
            r[-1] = "`python3 -c \"raise SystemExit(1)\"`"
            create_queue(root, [r])
        else:
            create_queue(root, [row("G01", "Record result", "in_progress", "None", "result.txt", "ready")])
    else:
        write(root / "REQUEST.md", "# Project request\n\nCreate a one-line greeting file and a separate one-line farewell file. Each should be independently verified.\n")
        write(root / "notes.txt", "Owner notes\n")
    if scenario == "archive":
        write(root / "goals/archive/2025-01-02-create-result.md", "# Unrelated existing archive\n\nPreserve this exact content.\n")
    git(root, "init", "-q")
    git(root, "config", "user.name", "Fixture User")
    git(root, "config", "user.email", "fixture@example.invalid")
    git(root, "add", ".")
    git(root, "commit", "-qm", "Fixture baseline")
    if scenario == "legacy-dirty":
        index = root / "goals/index.md"
        index.write_text(index.read_text(encoding="utf-8").replace("[x] [G01", "[ ] [G01"), encoding="utf-8")
        write(root / "unrelated.txt", "Unrelated user edit\n")
    if scenario == "interrupted":
        write(root / "result.txt", "ready\n")

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("scenario", choices=("fresh", "legacy-dirty", "queue", "failure", "interrupted", "archive"))
    parser.add_argument("destination", type=Path, help="path that does not yet exist")
    args = parser.parse_args()
    if args.destination.exists() or args.destination.is_symlink():
        parser.error("destination already exists")
    materialize(args.destination.resolve(), args.scenario)
    print(f"Created {args.scenario} in {args.destination}")

if __name__ == "__main__":
    main()
