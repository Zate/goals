# Goals plugin execution queue

Build and verify one portable Goals skill for Codex and Claude Code. The [PRD](../PRD.md) defines behavior and the [plan](../PLAN.md) defines milestones. **G12 ends at a publish-ready candidate. G13–G14 cover publication and hosted verification.**

## Operating Rules

- Use queue order for serial execution and honor each goal's prerequisites. Resume an eligible in-progress goal before picking new work.
- Keep one focused commit per goal, including its status, index row and evidence. Stage only goal-owned paths and review the staged diff. Finish integrating one goal before applying the next.
- Treat a request for the next goal as a one-goal run. Use parallel work only when the execution request authorizes a multi-goal run. The coordinating agent owns the queue, integration order and commits.
- Preserve existing user changes. The queue provides no authority to publish, use a paid account, install into normal host profiles, or alter other repositories.

## Model And Token Guidance

Use higher reasoning for the queue contract, recovery, packaging schemas and release review. Use standard coding models for well-scoped tooling and fixtures. Give workers their goal file, relevant PRD requirements and an explicit path or artifact boundary. Return checks, evidence and unresolved issues with each handoff.

## Goal File Format

Each linked file identifies status, objective, source, prerequisites, scope, non-goals, implementation notes, acceptance criteria, definition of done and verification. Prerequisites refer to stable IDs. Status values are `planned`, `in_progress`, `blocked`, `complete` and `retired`. Check off completed goals. Keep blocked goals unchecked and add blocker, attempted recovery and input needed.

## Execution Loop

1. Read the target goal, source requirements and repository guidance. Inspect Git status and prerequisite commits and reconcile any disagreement between a status, checkbox and existing work.
2. Mark the selected goal `in_progress`. Agree on file ownership before delegation. Workers use isolated workspaces or disposable fixtures and return patches or evidence. Only the coordinator updates shared queue files.
3. Implement the goal, run its focused checks and the established repository gates. Confirm the result through the normal entry point.
4. Record commands, results and remaining limitations. Set the goal to `complete`, check off its row, run `git diff --cached --check` after staging and commit the goal. Confirm the resulting status.
5. In an all-goals run, continue with eligible work. Skip goals with unmet prerequisites and stop for a queue-wide blocker or the release authorization checkpoint.

## Sequencing and delegation

| Group | Goals | Execution and ownership |
| --- | --- | --- |
| Foundation | G01 → G02 | Serial. Set the legacy baseline and queue contract before changing the shared entry point and references. |
| Package and fixtures | G03, G04, G05 | After G02, three independent workers can own platform manifests and presentation metadata, installer and its tests, and behavioral fixtures respectively. Integrate in queue order. |
| Release tooling | G06 → G07 | Validator consumes both package and installer outputs. CI consumes tested command interfaces. Fixture work can continue independently of these gates. |
| Host lifecycle | G08, G09 | After G07, run Codex and Claude Code checks in parallel against one candidate with separate temporary profiles and copies. Workers submit separate evidence. |
| Behavior | G10 | Retired by user direction after both hosts' managed marketplace policies prevented authenticated local trials. Behavioral and cross-host evidence remains unverified. |
| Readiness | G11 → G12 | Serial. Reconcile docs and confirmed public metadata, then check the resulting candidate and assemble evidence. |
| Publication | G13 → G14 | Maintainer authorization is required before G13. After publication, hosted CI and the two remote installation checks can run concurrently against the same revision. |

## Definition Of Done

- All goal acceptance criteria pass and required evidence is reviewable.
- Focused tests or fixture checks cover the changes. Update relevant docs and record any checks that could not run. An unavailable required gate leaves the goal open.
- Goal status and index checkbox agree, unrelated changes are preserved, and temporary artifacts are cleaned up.
- One focused Git commit contains the goal's deliverables and queue updates.

## Verification

Before release tooling lands, use each goal's file and fixture checks plus `git diff --check` and `git diff --cached --check`. This planning baseline has no existing build, lint or test command. The queue was checked for link resolution, valid goal sections and statuses, unique ordered IDs, valid prerequisites and coverage of all eight milestones.

As tools land, run `python3 -B -m unittest discover -s tests -v`, `python3 -B scripts/validate_release.py`, and `python3 -B scripts/install_agent_skills.py --dry-run --target <disposable-target>` from the repository root. The release validation guide will specify the pinned Agent Skills validator and host-specific checks. Keep authenticated trials separate from deterministic CI. Record source revision, package version and host/model details where relevant.

## Blocking And Recovery

Preserve work and record the exact blocking condition and checks attempted. If a run was interrupted after verification, inspect its changes and completion evidence before resuming. Re-run missing checks and finish the status or commit update when authorized. If a blocker affects only one goal, keep its dependents pending and proceed with independent eligible work in an all-goals run. Report a queue-wide blocker and the decision or input required.

## Queue

- [x] [G01 - Capture legacy compatibility](01-legacy-compatibility.md)
- [x] [G02 - Refine the portable skill](02-portable-skill.md)
- [x] [G03 - Package the two marketplaces](03-marketplace-packaging.md)
- [x] [G04 - Build the standalone installer](04-standalone-installer.md)
- [x] [G05 - Specify behavioral evaluation fixtures](05-behavioral-fixtures.md)
- [x] [G06 - Validate the release package](06-release-validator.md)
- [x] [G07 - Gate releases in cross-platform CI](07-cross-platform-ci.md)
- [x] [G08 - Verify the Codex install lifecycle](08-codex-lifecycle.md)
- [x] [G09 - Verify the Claude Code install lifecycle](09-claude-lifecycle.md)
- [ ] [G10 - Verify installed skill behavior](10-installed-behavior.md) — retired by user direction
- [x] [G11 - Finish public metadata and release docs](11-public-release-docs.md)
- [x] [G12 - Qualify the publish-ready candidate](12-release-readiness.md)
- [ ] [G13 - Publish the approved candidate](13-authorized-publication.md)
- [ ] [G14 - Verify the hosted release](14-hosted-verification.md)
