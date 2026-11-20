# G01 - Capture legacy compatibility

Status: complete

Prerequisites: None

## Objective

Keep a reproducible baseline of the existing queue so changes to behavior can be reviewed against real examples.

## Source / context

[Delivery plan](../PLAN.md) M1 and [PRD](../PRD.md) R1–R7.

## Scope

- Add a small legacy queue fixture and a compatibility note. Record this checkout as the local implementation workspace.

## Non-goals

- Portable skill changes and remote repository selection.

## Implementation notes

- Include a planned goal, a checked completed goal, a blocked goal and archived history. Use the existing index and goal conventions. Capture current mode routing, status repair, and commit and resume rules before changing the skill.

## Acceptance criteria

- Every existing mode and status maps to retained or intentionally revised behavior. The note identifies how checkbox disagreements, dependency-free queues and commit boundaries carry forward.
- The fixture works as a disposable consumer repository and contains no personal paths or credentials.

## Definition of done

- Acceptance criteria pass and verification results are recorded.
- Focused tests or fixture checks and relevant docs reflect the change.
- Status is `complete`, the index row is checked, and the goal has one focused commit.

## Verification

- Resolve every fixture queue and archive link. Check filenames, stable IDs, statuses and archive metadata against the original skill. Walk the fixture using the original rules and compare the observations to the note.

## Completion notes

- Copied the fixture to a temporary consumer directory and checked queue and archive links, unique IDs, goal sections, statuses, archive metadata, and the original selection rule with both a checked and an unchecked completed goal. All checks passed.
- `git diff --check` passed. The baseline is synthetic and does not establish host behavior.
