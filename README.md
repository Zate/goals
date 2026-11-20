# Goals

Goals helps a coding agent turn a plan into a repository-local queue of
verifiable outcomes, report progress, execute or resume work, and archive or
retire goals. The queue uses Markdown files under `goals/`, so a person or
another agent can inspect the work and its verification.

The shared skill is available through Codex and Claude Code marketplaces or as
a standalone Agent Skill. It supports existing queues without dependency fields
and new goals with optional prerequisite IDs.

## Install from a local checkout

Use the absolute path to this repository as `<checkout>`. Start a new agent
session after installation so the host loads the skill.

### Codex

```sh
codex plugin marketplace add "<checkout>"
codex plugin add goals@goals-marketplace
codex plugin list --marketplace goals-marketplace
```

### Claude Code

```sh
claude plugin marketplace add "<checkout>"
claude plugin install goals@goals-marketplace
claude plugin details goals@goals-marketplace
```

## Install from GitHub

The intended GitHub marketplace is `Zate/goals`. These commands apply after
the repository is published and the hosted installation checks have passed.

### Codex

```sh
codex plugin marketplace add Zate/goals
codex plugin add goals@goals-marketplace
codex plugin list --marketplace goals-marketplace
```

### Claude Code

```sh
claude plugin marketplace add Zate/goals
claude plugin install goals@goals-marketplace
claude plugin details goals@goals-marketplace
```

Hosted installation still awaits release verification. See the
[validation guide](docs/validation.md) for the checks and evidence.
Authenticated local marketplace use is subject to each host's managed policy.
Model-based behavior checks have been waived and remain unverified.

## Install the standalone skill

Choose a skill directory supported by your agent. The installer creates a
`goals` directory at the specified target and copies its references, examples,
and metadata.

```sh
python3 scripts/install_agent_skills.py --dry-run --target "<skills-directory>"
python3 scripts/install_agent_skills.py --target "<skills-directory>"
```

The installer reports a collision if `<skills-directory>/goals` already
exists. Review the existing installation before replacing or removing it. For
Windows, use the available Python command and a Windows path for the target.

If you previously copied the old single `goals/SKILL.md`, migrate by installing
the complete new skill directory, including `references/` and `assets/`.
Existing repository queues can continue to use their documented format.

## First session

Open a repository in a fresh Codex or Claude Code session and invoke the
installed skill explicitly.

```text
$goals Set up a goals queue for this repository.
/goals:goals Set up a goals queue for this repository.
```

Use the first line in Codex and the second in Claude Code. You can also ask in
natural language. To create goals from a plan, provide its path, for example
`Turn PLAN.md into executable goals.` Review the generated `goals/index.md`
and goal files before requesting execution.

These requests select common modes:

```text
What is the status of the goals?
Work on the next eligible goal.
Work through all eligible goals.
Resume the in-progress goal.
Archive completed goals.
```

Status inspection reports inconsistencies without modifying the queue.
Execution records verification and respects the repository's instructions.
Request a commit explicitly when one is wanted.

## Refresh and uninstall

For a local Codex marketplace, re-add the plugin after changing the checkout.
```sh
codex plugin add goals@goals-marketplace
codex plugin remove goals@goals-marketplace
codex plugin marketplace remove goals-marketplace
```

For a hosted Codex marketplace, refresh the marketplace before re-adding the
plugin.

```sh
codex plugin marketplace upgrade goals-marketplace
codex plugin add goals@goals-marketplace
```

For Claude Code, update the marketplace and plugin, or uninstall them.

```sh
claude plugin marketplace update goals-marketplace
claude plugin update goals@goals-marketplace
claude plugin uninstall goals@goals-marketplace
claude plugin marketplace remove goals-marketplace
```

Start a new session after changing an installation. In a running Claude Code
session, `/reload-plugins` reloads installed plugins.

## Troubleshooting

- If the skill does not appear, inspect the host's plugin list or details and
  start a new session. Confirm the marketplace points to the intended checkout.
- If standalone installation reports an existing destination, inspect that
  directory and choose an empty target or remove the old installation after
  review.
- If a queue has missing links, inconsistent statuses, or blocked
  prerequisites, ask for goal status first. The report identifies the
  affected work without changing files.
- If validation fails, run the checks in the [validation guide](docs/validation.md)
  and inspect the reported path or field.

## Release and security

The [release checklist](docs/release-checklist.md) describes the evidence and
approval needed for a release. Goals is licensed under MIT. Report security
issues privately through a GitHub security advisory for the repository when
available. Keep secrets, private repository contents and customer data out of
public issues.
