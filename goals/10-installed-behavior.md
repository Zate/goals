# G10 - Verify installed skill behavior

Status: retired

Prerequisites: G05, G08, G09

## Objective

Prove the installed skill can manage the same queue in both hosts.

## Source / context

[Delivery plan](../PLAN.md) M5, M6 and [PRD](../PRD.md) R1–R8.

## Scope

- Run G05 cases in the isolated installs. Own the behavior evidence and any minimal runner needed for repeatable cases.

## Non-goals

- Hosted CI runs, default-profile changes and release publication.

## Implementation notes

- Use the same package version and record host/model/revision per run. Independent cases may run in parallel. Run cross-host resume in sequence with the same disposable repository. Run unassisted controls on activation-sensitive cases. Repeat ambiguous outcomes and review differences.

## Acceptance criteria

- Every applicable case passes on each host. Evidence includes file and Git comparisons and rubric judgments, with explicit and natural-language activation covered.
- A second host resumes verified or interrupted work without replaying completed changes. Reports distinguish actual changes from host messages.

## Definition of done

- Acceptance criteria pass and verification results are recorded.
- Focused tests or fixture checks and relevant docs reflect the change.
- Status is `complete`, the index row is checked, and the goal has one focused commit.

## Verification

- Follow the G05 case protocol, independently check filesystem and Git observations, and record verdicts and discrepancies in `docs/validation.md`. Verify any fixes with targeted reruns before accepting the revised package.

## Retirement notes

- The user directed that both Codex and Claude model evaluations be skipped after their authenticated local marketplace attempts were denied by enterprise policy. None of the model behavior cases or cross-host recovery were run.
- G11 and G12 may proceed with this explicit waiver recorded as a release limitation. Reopen this goal if an approved test route becomes available.
