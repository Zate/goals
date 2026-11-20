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
