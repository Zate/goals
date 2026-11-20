# G02 - Refine the portable skill

Status: complete

Prerequisites: G01

## Objective

Ship a single self-contained skill capable of operating fresh and legacy queues.

## Source / context

[Delivery plan](../PLAN.md) M2 and [PRD](../PRD.md) R1–R7.

## Scope

- Move only the original skill to `plugins/goals/skills/goals/SKILL.md`. Keep this execution queue in root `goals/`. Add mode references, index and goal examples, and migration instructions for prior standalone users.

## Non-goals

- Marketplace packaging and host validation.

## Implementation notes

- Define a portable dependency syntax keyed by stable ID, including missing links and cycles. Use existing queue order when dependencies are absent. Keep routing, read-only status and authorization at the entry point. Document evidence-backed recovery for interrupted writes, failed checks and missing commits. Repair the historical link in the PRD if needed.

## Acceptance criteria

- Setup is idempotent, explicit conversion creates traceable atomic goals, and unrelated autonomy or planning-only requests leave the queue untouched.
- Status is read-only. Next and all honor prerequisites and distinct stopping points. Verification and authorization determine when completion and commits are allowed.
- Recovery preserves user changes and avoids replay. Archive and retirement preserve goal identity, content and discoverability, including on a collision or retry.

## Definition of done

- Acceptance criteria pass and verification results are recorded.
- Focused tests or fixture checks and relevant docs reflect the change.
- Status is `complete`, the index row is checked, and the goal has one focused commit.

## Verification

- From the packaged directory alone, walk R1–R7 with the shipped templates and G01 fixture. Traverse all bundled references and check examples against the documented state transitions and execution order.

## Completion notes

- Walked R1–R7 against the packaged instructions, templates and G01 fixture, including a status mismatch, failed verification and an archive collision. Verified all packaged Markdown links and template references.
- `git diff --check` passed. The optional skill-creator quick validator could not run because PyYAML is unavailable. Host behavior remains subject to G10.
