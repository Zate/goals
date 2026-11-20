# Release validation

Run the deterministic checks from the repository root with Python 3. The first
three commands need no model credentials or network access. Choose a disposable
target that does not already contain a `goals` directory.

```sh
python3 -B scripts/validate_release.py
python3 -B -m unittest discover -s tests -v
python3 -B scripts/install_agent_skills.py --dry-run --target /path/to/disposable/skills
```

The release validator checks catalog identity and paths, matching versions,
plugin skill paths, bundled resources, Markdown links and sample queue fields.
The tests seed broken versions, paths, resources and template links in temporary
copies. Installer tests cover dry-run, collision preservation, copy failure and
a complete byte-for-byte installation.

## Agent Skills reference validation

The reference validator is pinned to Agent Skills commit
`69ef37e9424c0a7ea9dd2293b559e43ec8176379`. Installing it needs Git and
network access to GitHub and a Python package index. Use a disposable virtual
environment and skills target.

```sh
python3 -m venv /path/to/disposable/venv
/path/to/disposable/venv/bin/python -m pip install 'git+https://github.com/agentskills/agentskills.git@69ef37e9424c0a7ea9dd2293b559e43ec8176379#subdirectory=skills-ref'
python3 -B scripts/install_agent_skills.py --target /path/to/disposable/skills
PATH="/path/to/disposable/venv/bin:$PATH" python3 -B scripts/validate_skills_ref.py --skill /path/to/disposable/skills/goals
```

On Windows use the virtual environment's `Scripts\python.exe` and add its
`Scripts` directory to `PATH`. `scripts/validate_skills_ref.py` defaults to
the source skill when `--skill` is omitted. The installed-tree check above
also verifies that standalone copying included the validator's inputs.

## Claude manifest checks

With the Claude Code CLI available, validate both manifest roots.

```sh
claude plugin validate --strict --json .
claude plugin validate --strict --json plugins/goals
```

Inspect the manifest errors and warnings as well as the exit status. The plugin
directory report can include separate directory submission findings. Local and
hosted marketplace installation evidence is recorded as it becomes available.

## Continuous integration

The release workflow runs the package validator, unit tests, standalone installer
dry-run and pinned Agent Skills reference validator on Ubuntu and Windows.
Checkout and Python setup actions are pinned to commits. The reference validator
installation uses Git and downloads from GitHub and a Python package index.
The runner's temporary directory holds the installer dry-run target. These checks
do not require host profiles or model credentials. Hosted run evidence will be
recorded with the published revision.

## Local marketplace lifecycle, partial

On 2026-11-20, disposable source copies from commit
`03720deddc274d977818d2296d0ec58e7daccec3` and isolated host profiles were
used on macOS. Both hosts installed version 0.1.0 and the installed skill tree
matched the source filenames and SHA-256 hashes. Temporary profiles were removed.

- Codex CLI 0.170.0 added the local marketplace, installed and listed one
  enabled plugin, removed it, and reinstalled it. A fixture version 0.1.1 was
  refreshed by re-running `codex plugin add`. Marketplace upgrade rejected the
  local source. Read-only signatures of the normal Codex configuration and
  plugin tree matched before and after.
- Claude Code 2.1.311 passed strict marketplace and plugin manifest validation,
  added the local marketplace and installed one skill. A fixture version 0.1.1
  appeared after marketplace and plugin update. Uninstall produced an empty
  list and reinstall restored 0.1.1. Normal-profile signatures were not checked.

Fresh-session model invocation and reference resolution remain unverified for
both hosts. These partial results do not complete G08 or G09.

The subsequent authorized fresh-session trials on 2026-11-20 did not reach a
model response. Codex CLI 0.170.0 rejected both the workspace marketplace and
a disposable copy under its `enterprise-managed requirements pilot`. Claude
Code 2.1.311 returned a 401 for an expired OAuth access token. Claude's normal
configuration, settings and plugin-state signatures matched before and after
the isolated trial. Both tests removed their temporary profiles and credentials.

The user subsequently directed that the Codex authenticated evaluation be
skipped. This leaves Codex skill invocation, reference loading and the Codex
portion of cross-host behavior unverified.

After authentication was refreshed, Claude's authenticated marketplace add
returned exit 1 because the local directory source was blocked by enterprise
policy. The earlier successful lifecycle used a temporary home and therefore
does not establish that the marketplace is permitted under the authenticated
account's policy. The user directed that Claude model checks also be skipped.
No model behavior or cross-host recovery has been verified.
