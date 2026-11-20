# G14 - Verify the hosted release

Status: planned

Prerequisites: G13

## Objective

Show that CI and both real marketplace installs pass for the published candidate.

## Source / context

[Delivery plan](../PLAN.md) M8 and [PRD](../PRD.md) R8.

## Scope

- Collect the hosted Ubuntu/Windows results and run remote marketplace add, install, inventory and first invocation in fresh Codex and Claude Code profiles.

## Non-goals

- Additional publication or remote changes without authorized release scope.

## Implementation notes

- The CI and host checks can run in parallel against the same published revision. Compare remote resolved revision, package version and installed hashes against G12/G13. If anything fails, record host and stage and requalify any corrected candidate before renewed publication.

## Acceptance criteria

- Both CI jobs pass. Each host loads the expected version and tree, and first invocation discovers and uses the skill. Dated evidence records exact commands, platform, host version and links to the run and published source.

## Definition of done

- Acceptance criteria pass and verification results are recorded.
- Focused tests or fixture checks and relevant docs reflect the change.
- Status is `complete`, the index row is checked, and the goal has one focused commit.

## Verification

- Verify hosted job results for the released revision and rerun both remote install sequences in isolated profiles. Confirm normal profile signatures match and remove the smoke-test artifacts.
