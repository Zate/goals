from __future__ import annotations

import hashlib
import importlib.util
import io
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "install_agent_skills.py"
SPEC = importlib.util.spec_from_file_location("install_agent_skills", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
INSTALLER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(INSTALLER)


def tree_hashes(root: Path) -> dict[str, str]:
    return {
        str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in root.rglob("*")
        if path.is_file()
    }


class InstallerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="tmp_rovo_install_")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.target = self.root / "path with spaces" / "skills"

    def test_dry_run_creates_no_paths(self) -> None:
        output = io.StringIO()
        result = INSTALLER.install_skill(INSTALLER.SKILL_SOURCE, self.target, dry_run=True, output=output)
        self.assertEqual(self.target.resolve() / "goals", result)
        self.assertIn(str(result), output.getvalue())
        self.assertFalse(self.target.parent.exists())

    def test_cli_installs_complete_tree_in_path_with_spaces(self) -> None:
        run = subprocess.run(
            [sys.executable, "-B", str(SCRIPT), "--target", str(self.target)],
            text=True, capture_output=True, check=True,
        )
        self.assertIn(str((self.target / "goals").resolve()), run.stdout)
        self.assertEqual(tree_hashes(INSTALLER.SKILL_SOURCE), tree_hashes(self.target / "goals"))
        source_dirs = {
            path.relative_to(INSTALLER.SKILL_SOURCE)
            for path in INSTALLER.SKILL_SOURCE.rglob("*") if path.is_dir()
        }
        installed = self.target / "goals"
        installed_dirs = {
            path.relative_to(installed) for path in installed.rglob("*") if path.is_dir()
        }
        self.assertEqual(source_dirs, installed_dirs)

    def test_collision_preserves_existing_destination(self) -> None:
        existing = self.target / "goals"
        existing.mkdir(parents=True)
        (existing / "keep.txt").write_text("keep", encoding="utf-8")
        before = tree_hashes(self.target)
        with self.assertRaisesRegex(INSTALLER.InstallError, "already exists"):
            INSTALLER.install_skill(INSTALLER.SKILL_SOURCE, self.target, output=io.StringIO())
        self.assertEqual(before, tree_hashes(self.target))

    def test_partial_copy_failure_removes_only_created_skill(self) -> None:
        self.target.mkdir(parents=True)
        marker = self.target / "existing.txt"
        marker.write_text("keep", encoding="utf-8")

        def fail_copy(source: Path, destination: Path, **kwargs: object) -> None:
            (destination / "partial.txt").write_text("partial", encoding="utf-8")
            raise OSError("copy failed")

        with patch.object(INSTALLER.shutil, "copytree", side_effect=fail_copy):
            with self.assertRaisesRegex(OSError, "copy failed"):
                INSTALLER.install_skill(INSTALLER.SKILL_SOURCE, self.target, output=io.StringIO())
        self.assertFalse((self.target / "goals").exists())
        self.assertEqual("keep", marker.read_text(encoding="utf-8"))

    def test_target_is_required(self) -> None:
        run = subprocess.run([sys.executable, "-B", str(SCRIPT)], text=True, capture_output=True)
        self.assertNotEqual(0, run.returncode)
        self.assertIn("--target", run.stderr)


if __name__ == "__main__":
    unittest.main()
