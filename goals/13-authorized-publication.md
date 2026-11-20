# G13 - Publish the approved candidate

Status: complete

Prerequisites: G12

## Objective

Make the exact approved candidate available at the chosen hosted marketplace source.

## Source / context

[Delivery plan](../PLAN.md) M8 and [PRD](../PRD.md) R8.

## Scope

- Obtain explicit release authorization for the destination, version and revision. Publish by the confirmed mechanism and record the result.

## Non-goals

- Publication on implicit authority and final hosted acceptance before G14.

## Implementation notes

- G13 is the authorization checkpoint. If approval is absent, stop the release path and record what is needed. Reconfirm what will be published if source or version changed after qualification. Keep evidence commits separate from package changes.

## Acceptance criteria

- The remote source resolves to the authorized revision and version. The release record identifies the destination, tested payload and remote CI run, when observable.

## Definition of done

- Acceptance criteria pass and verification results are recorded.
- Focused tests or fixture checks and relevant docs reflect the change.
- Status is `complete`, the index row is checked, and the goal has one focused commit.

## Verification

- Use read-only inspection to resolve the remote ref and compare it with the approved candidate. Record the reference and version. Review the staged local publication record before committing it.

## Completion notes

- With explicit user approval, created the public `https://github.com/Zate/goals` repository and pushed `main`. After the user refreshed GitHub CLI authorization with the required workflow scope, `git ls-remote` resolved `main` to the approved `7afad4b4adb749c33cd8e543d661aa97c5168ac1`. The qualified package source is `99e309c94b09857f66a499c9363c4cbce4a70c94`, version 0.1.0.
- Hosted validation run `https://github.com/Zate/goals/actions/runs/44735618658` started for the published revision. G14 records its result and hosted installation evidence.
