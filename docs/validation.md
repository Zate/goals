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

Fresh-session trials on 2026-11-20 stopped before either host returned a model
response. Codex rejected both the checkout marketplace and a disposable copy.
Claude's first attempt returned HTTP 401. On retry, the local marketplace add
exited with status 1. Claude's normal configuration, settings and plugin-state
signatures matched before and after the isolated trial. Temporary profiles and
credentials were removed.

Further model checks were waived for both hosts. Live skill invocation,
reference loading and cross-host recovery remain unverified.

## Candidate qualification evidence

On 2026-11-20, a disposable archive of commit
`99e309c94b09857f66a499c9363c4cbce4a70c94` was checked on macOS. The
manifest version is `0.1.0`. The archive, installed skill and disposable
validator environment were removed after the checks.

| Check | Result |
| --- | --- |
| `python3 -B scripts/validate_release.py` | Passed |
| `python3 -B -m unittest discover -s tests -v` | Passed, 14 tests |
| `python3 -B scripts/install_agent_skills.py --dry-run --target <temporary path with spaces>` | Passed |
| `python3 -B scripts/install_agent_skills.py --target <temporary path with spaces>` | Passed, seven skill files matched the source paths and SHA-256 hashes |
| Pinned Agent Skills validator `69ef37e9424c0a7ea9dd2293b559e43ec8176379` against the standalone installed skill | Passed |
| `claude plugin validate --strict --json <archive root>` | Passed with no marketplace manifest errors or warnings |
| `claude plugin validate --strict --json <archive root>/plugins/goals` | Passed with no plugin manifest errors or warnings. Its directory report flagged a README missing because the archive had no Git root, and an optional icon |

The skill tree digest was
`5d6287e14de8678fcaf28f4840d481417a7a582d6e79bb3e4a3d9ce254df9137`.
The digest is SHA-256 over the concatenation of sorted relative path strings
and each file's SHA-256 hex digest. The installed tree matched the source
tree by individual path and hash.

### Requirement evidence and limits

| Requirement | Evidence |
| --- | --- |
| R1 | Setup and repeated setup are specified in the skill and G05 A1. The host behavior trial was waived. |
| R2 | Planning and stable IDs are specified in the skill and G05 A1–A3. The host behavior trials were waived. |
| R3 | Read-only status is specified in the skill and G05 S1. The host behavior trial was waived. |
| R4 | Selection, checks and commit authorization are specified in the skill and G05 E1, E2 and X1. The host behavior trials were waived. |
| R5 | Independent work and blocked dependencies are specified in the skill and G05 E1. The host behavior trial was waived. |
| R6 | Recovery is specified in the skill and G05 S1 and X1. Cross-host recovery was not tested. |
| R7 | Archival and retirement are specified in the skill and G05 A4. The host behavior trial was waived. |
| R8 | Package validation, standalone install and unauthenticated local marketplace lifecycle checks passed. The lifecycle record in `validation.md` covers source `03720de`; the later G11 local recheck used the 99e309c package inputs before its commit. Neither fresh-session trial reached model invocation. |

The checks above establish package structure and local installation,
while actual model behavior, reference loading and cross-host recovery remain
unverified. Hosted CI and remote marketplace installs remain pending.
