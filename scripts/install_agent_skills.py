#!/usr/bin/env python3
"""Install the bundled Goals skill into an explicitly selected directory."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path
from typing import TextIO


SKILL_SOURCE = Path(__file__).resolve().parents[1] / "plugins" / "goals" / "skills" / "goals"


class InstallError(RuntimeError):
    """Installation cannot proceed without risking existing data."""


def install_skill(
    source: Path, target: Path, *, dry_run: bool = False, output: TextIO = sys.stdout
) -> Path:
    """Copy the complete skill into target/goals, preserving existing files."""
    source = source.expanduser().resolve()
    target = target.expanduser().resolve()
    destination = target / "goals"

    if not source.is_dir() or not (source / "SKILL.md").is_file():
        raise InstallError(f"Goals skill source is missing or invalid: {source}")
    if any(path.is_symlink() for path in source.rglob("*")):
        raise InstallError(f"Goals skill source contains a symbolic link: {source}")
    if target.exists() and not target.is_dir():
        raise InstallError(f"Install target is not a directory: {target}")
    if target == source or source in target.parents or target in source.parents:
        raise InstallError("Skill source and install target must not contain each other")
    if destination.exists() or destination.is_symlink():
        raise InstallError(f"Destination already exists; choose another target: {destination}")

    action = "Would install" if dry_run else "Installing"
    print(f"{action} {source} -> {destination}", file=output)
    if dry_run:
        return destination

    target.mkdir(parents=True, exist_ok=True)
    try:
        destination.mkdir()
    except FileExistsError as error:
        raise InstallError(f"Destination already exists; choose another target: {destination}") from error

    try:
        shutil.copytree(source, destination, dirs_exist_ok=True)
    except Exception:
        shutil.rmtree(destination)
        raise
    return destination


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--target", type=Path, required=True, help="Directory in which to create the goals skill"
    )
    parser.add_argument("--dry-run", action="store_true", help="Report paths without writing")
    args = parser.parse_args(argv)

    try:
        install_skill(SKILL_SOURCE, args.target, dry_run=args.dry_run)
    except InstallError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    except OSError as error:
        print(f"error: installation failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
