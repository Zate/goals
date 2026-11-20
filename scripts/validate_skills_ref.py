#!/usr/bin/env python3
"""Validate the bundled skill with the Agent Skills reference validator."""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "plugins/goals/skills/goals"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill", type=Path, default=SKILL, help="Skill directory to validate")
    args = parser.parse_args()
    executable = shutil.which("skills-ref")
    if executable is None:
        print("error: skills-ref is unavailable; see docs/validation.md", file=sys.stderr)
        return 2
    return subprocess.run([executable, "validate", str(args.skill)], check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
