---
name: goals
description: Use when the Goals skill is explicitly invoked, when asked whether to use a repository-local goal queue, or when asked to initialize, plan, inspect, execute, resume, archive, or retire repository-local goals.
---

# Goals

Use a repository's `goals/index.md` and linked Markdown goal files to plan and
track work. Route by what the user asks for. Invoking the skill by itself does
not authorize changes.

- **Bare invocation** — Read the available repository guidance and planning
  context. If a queue exists, use the inspect guidance in
  [execution](references/execution.md). Summarize the current context and
  recommend one concrete next step with a brief reason. If the queue is absent,
  say so and base the recommendation on the available context. Keep this
  read-only, including Git state.
- **Workflow question** — Answer the specific question, such as whether the
  work benefits from a goal queue, using relevant context. Keep the response
  advisory and read-only.
- **Specific task** — Carry out the requested task directly. Use the matching
  mode below for a queue operation. A general request for autonomous work, a
  roadmap, or a plan for later conversion does not itself request a goal queue
  or authorize goal execution.

## Queue operations

- **Initialize or plan** — Read [planning](references/planning.md) to set up a
  queue or turn a source into goals.
- **Status** — Read [execution](references/execution.md) and report state
  without changing files, Git state, or the queue, even if it is malformed.
- **Next, all, or resume** — Read [execution](references/execution.md) to
  reconcile existing work, choose eligible goals and record verification.
- **Archive or retire** — Read [archive](references/archive.md) to preserve
  identity and history while updating the queue.

Before modifying a repository, inspect its guidance, existing goals and Git
status when available. Respect its rules and preserve unrelated changes.
Resolve a conflict between local rules and the requested task before execution.
A request to execute goals authorizes in-scope work, while a commit, remote
write, installation, or other external action requires its own authorization.
When a commit is authorized, stage only the goal's changes. Never replay verified
work solely because its checkbox, status or commit is missing.

Existing queues and their documented order remain valid. New goals may declare
optional `Prerequisites: G01, G02` references by stable ID. Missing references,
duplicate IDs, cycles and checkbox/status disagreements must be reported. See
the mode references for selection, recovery and archive handling.
