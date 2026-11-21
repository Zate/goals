# Goals

![A mountain goat beside a trail map with a marked route to the summit.](assets/header.webp)

Give Codex or Claude Code a plan, then ask it to work through one goal at a
time. Goals keeps the queue, acceptance criteria, and verification notes in
your repository as plain Markdown. Open a fresh session and you can see
what passed, what’s blocked, and where to pick up.

[![Codex marketplace](https://img.shields.io/badge/Codex-marketplace-185647?style=flat-square)](#codex)
[![Claude Code marketplace](https://img.shields.io/badge/Claude%20Code-marketplace-964A2C?style=flat-square)](#claude-code)
[![Standalone Agent Skill](https://img.shields.io/badge/Agent%20Skill-standalone-2E6C59?style=flat-square)](#standalone-skill)
[![MIT license](https://img.shields.io/badge/license-MIT-A46514?style=flat-square)](LICENSE)

[Install](#install) · [First session](#first-session) · [Example queue](#example-queue) · [Troubleshooting](#troubleshooting)

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

<details>
<summary>Install from GitHub</summary>


Use the same commands above with `Zate/goals` in place of `"<checkout>"`.
Hosted installation checks are tracked in the
[release goal](goals/14-hosted-verification.md). Each host's managed policy
can affect marketplace access.

</details>

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

Open the project you want to work on in a fresh session. Enter the skill name
in chat to get your bearings.

| Codex | Claude Code plugin |
| --- | --- |
| `$goals` | `/goals:goals` |

On its own, Goals inspects the queue and recommends one next step with a
reason. If there’s no queue yet, it looks for planning material and suggests
where to start. Both are read-only.

**From plan to first result.** Here’s a typical Codex session. In Claude Code,
use `/goals:goals` in place of `$goals`.

1. **Plan.** `$goals Turn PLAN.md into executable goals.` Review the proposed work in `goals/index.md` and the files it links to.
2. **Execute.** `$goals Work on the next eligible goal.` The agent picks one goal, runs its checks, records the outcome, and stops. Ask explicitly if you want a commit.
3. **Pick up later.** `$goals Show me the status of the goals.` See what’s complete and what’s eligible. If work was interrupted, ask Goals to resume. It checks the files and verification notes before continuing.

You can also ask a question. Try `$goals How do next and all differ?` for an
explanation. Ask it to *work through all eligible goals* when you want it to
continue beyond the first one. Other requests include setting up an empty
queue and archiving completed goals.

## Example queue

Suppose your plan calls for a CSV export and a download button. Goals might
create this queue.

```text
goals/
├── index.md
├── 01-add-csv-export.md      G01 · Export filtered results as CSV
└── 02-add-export-button.md   G02 · Add a download button (requires G01)
```

The index shows the order. Open G01 to see what the export must do and how
to verify it. Once G01 passes its checks and is marked complete, G02 is
eligible. Prerequisites are optional for queues that only need an order.

**See a finished goal.** We used Goals to build its own standalone installer.
The goal records five passing tests, including a file-by-file comparison of
the installed skill with its source. You can follow that work from the
[PRD](PRD.md) through the [plan](PLAN.md) and [queue](goals/index.md) to the
[completed installer goal](goals/04-standalone-installer.md).

## Refresh and uninstall

<details>
<summary>Refresh an installation</summary>

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

</details>

<details>
<summary>Uninstall the plugin and marketplace</summary>

```sh
codex plugin remove goals@goals-marketplace
codex plugin marketplace remove goals-marketplace
```

```sh
claude plugin uninstall goals@goals-marketplace
claude plugin marketplace remove goals-marketplace
```

</details>

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
