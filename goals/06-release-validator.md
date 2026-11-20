# G06 - Validate the release package

Status: planned

Prerequisites: G03, G04

## Objective

Provide a repeatable local gate that detects broken manifests, skill resources and installers.

## Source / context

[Delivery plan](../PLAN.md) M4 and [PRD](../PRD.md) R8.

## Scope

- Own `scripts/validate_release.py`, the pinned Agent Skills validator invocation, and release validator negative tests. Add a documented command sequence.

## Non-goals

- Hosted CI wiring and authenticated testing.

## Implementation notes

- Reuse installer tests for collision checks. Seed invalid host paths and versions, missing resources and broken links in copies. Exercise bundled queue templates. Document the pinned dependency setup and strict Claude CLI validation separately from standard-library checks.

## Acceptance criteria

- A healthy package passes. Each seeded defect identifies the offending path or field. Standard package checks run without model credentials. Agent Skills validation covers the installed skill and Claude checks cover both manifests where available.

## Definition of done

- Acceptance criteria pass and verification results are recorded.
- Focused tests or fixture checks and relevant docs reflect the change.
- Status is `complete`, the index row is checked, and the goal has one focused commit.

## Verification

- Run `python3 -B scripts/validate_release.py`, `python3 -B -m unittest discover -s tests -v`, the documented pinned Agent Skills command and strict Claude validation when available. Confirm negative fixtures fail as expected.
