# G12 - Qualify the publish-ready candidate

Status: planned

Prerequisites: G06, G07, G08, G09, G10, G11

## Objective

Produce a reviewable publish-ready candidate and decision record.

## Source / context

[Delivery plan](../PLAN.md) M7 and [PRD](../PRD.md) R1–R8.

## Scope

- Tie deterministic, behavioral, isolated-install and documentation evidence to the proposed package. Record affected reruns and pending hosted gates.

## Non-goals

- Publishing, pushing commits and claiming hosted approval.

## Implementation notes

- Identify candidate version, source and installed payload. When the evidence record itself changes the commit hash, record the tested source and show that the candidate’s package and workflow inputs match it. Rerun gates affected by subsequent package or workflow changes.

## Acceptance criteria

- Every requirement links to passing evidence for the candidate. Local deterministic gates, both host lifecycle checks and required behavioral trials pass. A maintainer can identify the revision authorized for distribution and see hosted work due in G14.

## Definition of done

- Acceptance criteria pass and verification results are recorded.
- Focused tests or fixture checks and relevant docs reflect the change.
- Status is `complete`, the index row is checked, and the goal has one focused commit.

## Verification

- Run established local gates from a clean candidate checkout, check evidence against R1–R8 and verify package identity against recorded host results. Record the candidate revision and version for the release decision.
