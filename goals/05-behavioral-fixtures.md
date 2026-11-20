# G05 - Specify behavioral evaluation fixtures

Status: planned

Prerequisites: G02

## Objective

Provide shared, reproducible behavioral cases that both hosts can run in disposable consumer repositories.

## Source / context

[Delivery plan](../PLAN.md) M5 and [PRD](../PRD.md) R1–R8.

## Scope

- Own `evals/` prompts, starting states, expected changes, forbidden effects and rubric. Reference the legacy fixture where useful.

## Non-goals

- Authenticated eval runs and package or CI changes.

## Implementation notes

- Cover setup twice and explicit PRD conversion, planning-only and unrelated-goal language, dirty status and explicit recovery, next vs all, failed verification, missing/cyclic/blocked dependencies, interrupted completion and both commit policies, and archive collision or retry. Include explicit invocation, natural-language activation, unassisted comparison and a Codex-to-Claude or Claude-to-Codex resume case.

## Acceptance criteria

- Each case identifies what to inspect in outputs, file bytes and Git state, and which criteria require human review. No case relies on the developer machine or a network service to verify the consumer repo.

## Definition of done

- Acceptance criteria pass and verification results are recorded.
- Focused tests or fixture checks and relevant docs reflect the change.
- Status is `complete`, the index row is checked, and the goal has one focused commit.

## Verification

- Check every fixture link, materialize representative fresh and dirty fixtures in disposable repos, and review the case matrix against R1–R8 and the M5 scenario table.
