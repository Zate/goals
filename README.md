# Goals

![A mountain goat beside a trail map with a marked route to the summit.](assets/header.webp)

Goals is a skill for Codex and Claude Code. It turns a plan into a Markdown
queue in your repo so your agent can work through it across sessions.

[![Codex marketplace](https://img.shields.io/badge/Codex-marketplace-185647?style=flat-square)](#codex)
[![Claude Code marketplace](https://img.shields.io/badge/Claude%20Code-marketplace-964A2C?style=flat-square)](#claude-code)
[![Standalone Agent Skill](https://img.shields.io/badge/Agent%20Skill-standalone-2E6C59?style=flat-square)](#standalone-skill)
[![MIT license](https://img.shields.io/badge/license-MIT-A46514?style=flat-square)](LICENSE)

[Install](#install) · [First session](#first-session) · [Refresh or uninstall](#refresh-and-uninstall)

## Example

Ask your agent to turn `PLAN.md` into goals. A plan for CSV export might
produce these files.

```text
goals/
├── index.md
├── 01-add-csv-export.md      G01 · Export filtered results as CSV
└── 02-add-export-button.md   G02 · Add a download button (requires G01)
```

The index tracks the queue and its progress. Each goal file describes the
work, how to check it, and the results once those checks run. In this example,
the agent verifies the export before starting on the button. Prerequisites
are optional, so existing queues still work.

## Install

Use the absolute path to your Goals checkout in place of `<checkout>`. Start
a new agent session after installing.

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

### Install from GitHub

Use the same commands above with `Zate/goals` in place of `"<checkout>"`.
Hosted installation checks are tracked in the
[release goal](goals/14-hosted-verification.md). Each host's managed policy
can affect marketplace access.

### Standalone skill

Choose a skill directory supported by your agent. The installer copies the
complete skill into a `goals` subdirectory.

```sh
python3 scripts/install_agent_skills.py --dry-run --target "<skills-directory>"
python3 scripts/install_agent_skills.py --target "<skills-directory>"
```

If the target already contains a `goals` directory, the installer reports a
collision. On Windows, use your Python command and a Windows path. If you
previously copied just `goals/SKILL.md`, install the complete skill to get the
bundled references and templates.

## First session

Open the repository you want to work on in a fresh session. To start from a
plan, pass its path to the skill.

```text
$goals Turn PLAN.md into executable goals.
/goals:goals Turn PLAN.md into executable goals.
```

Use the first line in Codex and the second in Claude Code. If there is no
plan yet, ask the skill to set up an empty queue.

Review `goals/index.md` and the linked goal files before asking the agent to
start. You can also ask it to check progress or pick up interrupted work.

- “Show me the status of the goals.” This leaves the queue untouched.
- “Work on the next eligible goal” or “Work through all eligible goals.”
- “Resume the in-progress goal.”
- “Archive completed goals.”

Ask explicitly if you want the agent to commit its work.

## Refresh and uninstall

### Refresh

For a local Codex marketplace, re-add the plugin after changing the checkout.

```sh
codex plugin add goals@goals-marketplace
```

For a hosted Codex marketplace, refresh the marketplace before re-adding the
plugin.

```sh
codex plugin marketplace upgrade goals-marketplace
codex plugin add goals@goals-marketplace
```

For Claude Code, update the marketplace and plugin.

```sh
claude plugin marketplace update goals-marketplace
claude plugin update goals@goals-marketplace
```

Start a new session after refreshing. In Claude Code, you can also use
`/reload-plugins` in the current session.

### Uninstall

```sh
codex plugin remove goals@goals-marketplace
codex plugin marketplace remove goals-marketplace
```

```sh
claude plugin uninstall goals@goals-marketplace
claude plugin marketplace remove goals-marketplace
```

## Troubleshooting

- If the skill does not appear, check the host's plugin list and marketplace
  path, then start a new session.
- If the standalone installer reports a collision, review the existing copy
  or choose a different destination.
- If the queue has broken links, inconsistent statuses, or blocked goals,
  ask for goal status to see which files need attention.
- If validation fails, see the [validation guide](docs/validation.md) for the
  checks and their expected inputs.

## Release and security

See the [release checklist](docs/release-checklist.md) for release
requirements and the [validation guide](docs/validation.md) for test
results. Report security issues privately as described in the
[security policy](SECURITY.md). Goals is licensed under [MIT](LICENSE).
