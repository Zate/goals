# G07 - Gate releases in cross-platform CI

Status: planned

Prerequisites: G06

## Objective

Make the deterministic package checks repeatable on Ubuntu and Windows.

## Source / context

[Delivery plan](../PLAN.md) M4 and [PRD](../PRD.md) R8.

## Scope

- Own the GitHub Actions workflow. Run release validation, unit tests, installer dry-run and pinned Agent Skills validation on both runners.

## Non-goals

- Model evaluation, marketplace publication and claims of hosted success before G14.

## Implementation notes

- Use read-only workflow permissions, pinned dependencies/actions and runner-local temp paths. Keep shell and Python invocations portable and document any host binaries or network downloads used by the gates.

## Acceptance criteria

- Both CI jobs cover the full deterministic sequence. Neither host requires a personal profile or model credentials. The local sequence passes and hosted evidence is tracked for G14.

## Definition of done

- Acceptance criteria pass and verification results are recorded.
- Focused tests or fixture checks and relevant docs reflect the change.
- Status is `complete`, the index row is checked, and the goal has one focused commit.

## Verification

- Run every workflow command locally where supported. Validate workflow syntax and inspect the matrix, command quoting and permission scopes. Record unrun runner checks.
