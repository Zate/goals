"""Exercise release validation against independently damaged packages."""

import importlib.util
import json
import re
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("validate_release", ROOT / "scripts/validate_release.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class ReleaseValidationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="tmp_rovo_release_")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for name in (".agents", ".claude-plugin", "plugins"):
            shutil.copytree(ROOT / name, self.root / name)

    def assert_error(self, expected):
        errors = validator.validate_repository(self.root)
        self.assertTrue(any(expected in message for message in errors), errors)

    def change_json(self, name, change):
        path = self.root / name
        data = json.loads(path.read_text(encoding="utf-8"))
        change(data)
        path.write_text(json.dumps(data), encoding="utf-8")

    def test_valid_package(self):
        self.assertEqual(validator.validate_repository(self.root), [])

    def test_sample_queue_links_to_planned_goal_in_consumer(self):
        assets = self.root / "plugins/goals/skills/goals/assets"
        consumer = self.root / "consumer/goals"
        shutil.copytree(assets, consumer)
        index = (consumer / "index.md").read_text(encoding="utf-8")
        matches = re.findall(r"^- \[ \] \[(G\d+) - [^]]+\]\(([^)]+)\)$", index, re.M)
        self.assertEqual(len(matches), 1)
        goal_id, goal_path = matches[0]
        goal = (consumer / goal_path).read_text(encoding="utf-8")
        self.assertTrue(goal.startswith(f"# {goal_id} - "))
        self.assertIn("Status: planned", goal)
        self.assertIn("Prerequisites: None", goal)

    def test_version_drift(self):
        self.change_json("plugins/goals/.claude-plugin/plugin.json", lambda d: d.update(version="9.0.0"))
        self.assert_error("version")

    def test_codex_marketplace_path(self):
        self.change_json(".agents/plugins/marketplace.json", lambda d: d["plugins"][0]["source"].update(path="../escape"))
        self.assert_error("source.path")

    def test_claude_skill_path(self):
        self.change_json("plugins/goals/.claude-plugin/plugin.json", lambda d: d.update(skills="./missing/"))
        self.assert_error("skills")

    def test_missing_resource(self):
        (self.root / "plugins/goals/skills/goals/references/archive.md").unlink()
        self.assert_error("references/archive.md")

    def test_broken_template_link(self):
        path = self.root / "plugins/goals/skills/goals/assets/index.md"
        path.write_text(path.read_text(encoding="utf-8").replace("(goal.md)", "(missing.md)"), encoding="utf-8")
        self.assert_error("missing.md")

    def test_missing_template_field(self):
        path = self.root / "plugins/goals/skills/goals/assets/goal.md"
        path.write_text(path.read_text(encoding="utf-8").replace("## Verification", "## Checks"), encoding="utf-8")
        self.assert_error("## Verification")

    def test_invalid_manifest_shape_reports_error(self):
        self.change_json(".claude-plugin/marketplace.json", lambda d: d.update(plugins="bad"))
        self.assert_error("plugins")


if __name__ == "__main__":
    unittest.main()
