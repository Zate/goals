# Goals plugin product requirements

**Release outcome.** A developer can install Goals in Codex or Claude Code, turn an approved roadmap into a repository-local queue, finish one verified outcome, and resume from that same queue in the other host. The durable interface is ordinary Markdown a maintainer can read and edit. See the [milestone plan](PLAN.md) for sequencing and evidence.

## Starting point and benchmark

The [original skill](goals/SKILL.md) defines an index, goal files, five statuses, execution order, verification and archival. It tells status to repair obvious discrepancies, assumes one commit per goal, and selects the first unchecked item even when a checkbox disagrees with a completed file. Resuming after an interruption can therefore repeat work or change someone’s repository on an inspection request.

The comparison project, `golang-development`, provides four manifests around one shared payload, progressive skill references, Codex presentation metadata, a generic installer, release checks, cross-platform CI, shared behavioral evals, and dated marketplace smoke records. Its `docs/validation.md` distinguishes published 0.1.0 evidence from later local package and behavior checks. Goals needs equivalent evidence for its own workflows. The number of skills and Go-specific lint tooling are incidental to that benchmark.

## User workflows and acceptance

| ID | Request | Observable result |
| --- | --- | --- |
| R1 | “Set up goals here” | Create a usable index in the target repository. Running setup twice preserves existing goals, local instructions and edits. An occupied or ambiguous path is reported before modification. |
| R2 | “Turn this PRD into goals” | Each queued outcome links to its source, names its scope, dependencies, acceptance and verification. IDs are unique and stable on subsequent additions. A request for a PRD or milestones *for later conversion* produces only the requested planning documents. |
| R3 | “Where are we?” | Report counts, inconsistencies, blockers, active work and the next eligible goal. Comparing the workspace before and after shows zero edits, including on a malformed queue. |
| R4 | “Do the next goal” | Honor queue order and prerequisites, resume existing eligible work, verify the selected outcome and stop after that goal. Record the actual checks and their results. Commit only with authorization and include only goal-owned changes. |
| R5 | “Continue through all goals” | Repeat R4 while eligible work exists. A blocked prerequisite holds its dependents. Independent later work may proceed when the blocker is local to a goal. A decision affecting the remaining queue stops execution. Report skipped work and what would unblock it. |
| R6 | “Resume this queue” | Reconcile file status, checkbox, implementation and verification evidence before executing. Interrupted completion or a missing commit must never replay a verified change. Ambiguous conflicts leave user edits intact and identify the decision required. |
| R7 | “Retire this goal” or “Archive completed work” | Preserve content, stable identity, reason and discoverability. Update affected links and queue membership together. Repeating an archive operation creates no duplicate or overwrite. |
| R8 | “Install and try Goals” | Both hosts discover one Goals skill from the same versioned payload. From the README, a new user can install, invoke, inspect, refresh and remove it. The documented standalone install copies every required resource. |

## Queue compatibility and operating decisions

Retain the existing `goals/index.md`, linked Markdown goal files, five status values and archive convention. Existing queues without explicit dependencies follow their documented order and rules. Introduce optional dependency references by stable goal ID. Show unresolved references and cycles during status. Never silently rewrite a legacy queue. Respect repository-specific execution rules and identify conflicts before starting work.

A planned goal can become in progress, then complete after verification, or blocked with the attempted checks and missing input. Resume a blocked goal when its blocker clears. Retirement records why work closed without completion. Archiving changes location and queue membership while preserving the outcome. When committing is unavailable or unauthorized, record verified completion in the worktree and disclose the uncommitted state. If the repository expressly requires a commit for completion, report that remaining requirement. A failed check leaves the goal open. Treat an interrupted index/file update as a recovery case.

## Distribution and scope

Proposed public names are `goals` and `goals-marketplace`. Use one published skill with mode-specific references, portable examples/templates and an `agents/openai.yaml` entry. Keep the installed package self-contained. Host-specific descriptions and invocation examples belong in their respective metadata and user docs. Runtime operation requires only repository file access and the project’s own verification tools. A hosted service, background scheduler, host-native goal API, hooks and a new queue database are outside v1.

“Ready to publish” means an identified candidate passes the local package, installer, behavioral and two-host gates in the plan, with public metadata and release instructions reviewed. “Published and verified” additionally requires authorized distribution, hosted CI and fresh remote installs of that revision. Existing marketplace support in these requirements means installation from the project’s own catalog. Central directory listing or vendor endorsement is outside the acceptance criteria.

The maintainer must confirm the repository destination, public owner, license, security contact and release authority before distribution. Plan around a GitHub-hosted marketplace for parity with the reference. These decisions can wait while the skill and fixtures are developed.
