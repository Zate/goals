# G11 - Finish public metadata and release docs

Status: complete

Prerequisites: G08, G09, G10

## Objective

Give adopters a tested first-run path and maintainers a complete release checklist.

## Source / context

[Delivery plan](../PLAN.md) M7 and [PRD](../PRD.md) R8.

## Scope

- Add README, security contact, repo and package licenses, final public metadata and a release checklist. Cover local and hosted installs for both hosts, standalone use, invocation, status, upgrade, uninstall, migration and common failures.

## Non-goals

- Remote writes, hosted verification and a release announcement.

## Implementation notes

- Confirm destination, owner, license and security contact before adopting public values. Base local commands on G08/G09. Identify hosted commands awaiting G14. Include versioning, recovery from a bad release, release authorization and the evidence needed for a decision.

## Acceptance criteria

- README steps give each host a first successful local session and a documented standalone path. Package and repo licenses match. Public metadata and docs contain no machine paths or unresolved identity fields.

## Definition of done

- Acceptance criteria pass and verification results are recorded.
- Focused tests or fixture checks and relevant docs reflect the change.
- Status is `complete`, the index row is checked, and the goal has one focused commit.

## Verification

- Replay changed local install and use commands in disposable profiles. Check relative links and license parity and run package validation and unit tests. Review hosted syntax against official host docs.

## Completion notes

- Local marketplace add, install, inventory and removal were replayed in disposable unauthenticated profiles against the current package. Claude strict manifest checks passed. User-waived model invocation and authenticated enterprise policy checks remain unverified.
- Release validation and all 14 unit tests passed. Documentation links and identical MIT license copies were checked. Hosted commands await G14. `Zate/goals` follows the reference repository's owner and this project's name; its existence is unconfirmed.
