# Example project goals

Track the small example project.

## Operating Rules

- Work goals in queue order.
- Complete one goal per commit and finish the previous goal's commit before starting another.
- Stop when a decision or unsafe change blocks progress.

## Model And Token Guidance

Use the available model and read only files needed for the selected goal.

## Goal File Format

Each goal has a status, objective, source, scope, non-goals, implementation
notes, acceptance criteria, definition of done and verification.

## Execution Loop

Select the first unchecked nonblocked goal, implement and verify it, update its
status and checkbox, then commit. Repeat when all goals were requested.

## Definition Of Done

Acceptance criteria and verification pass, documentation is updated, the goal
and index are complete, and the change has a focused commit.

## Verification

Run the command listed in the selected goal from the repository root.

## Blocking And Recovery

Mark blocked goals with the blocker, attempts and needed input. Preserve changes
that do not belong to the selected goal.

## Queue

- [x] [G01 - Create result](01-create-result.md)
- [ ] [G02 - Add summary](02-add-summary.md)
- [ ] [G03 - Add external detail](03-add-external-detail.md)

## Archived

- [G04 - Retire old idea](archive/2025-01-01-retire-old-idea.md)
