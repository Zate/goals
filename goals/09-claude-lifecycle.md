# G09 - Verify the Claude Code install lifecycle

Status: complete

Prerequisites: G07

## Objective

Show that Claude Code can install, discover, update and remove the local Goals marketplace package.

## Source / context

[Delivery plan](../PLAN.md) M6 and [PRD](../PRD.md) R8.

## Scope

- Run the local smoke with isolated Claude configuration and plugin cache. Return Claude-only evidence for `docs/validation.md`.

## Non-goals

- Normal profile installs and remote marketplace testing.

## Implementation notes

- Use the same source payload as G08, with a separate disposable copy and consumer repo. Run strict validation at marketplace and plugin roots. Record CLI version, source revision and normal-profile signatures. Use a distinct fixture version for refresh.

## Acceptance criteria

- One installed skill is visible and works in a fresh session outside the source repo. Refresh exposes the distinct version. Uninstall and reinstall behave as expected. Installed hashes match the payload and normal profile signatures match.

## Definition of done

- Acceptance criteria pass and verification results are recorded.
- Focused tests or fixture checks and relevant docs reflect the change.
- Status is `complete`, the index row is checked, and the goal has one focused commit.

## Verification

- Run and record strict validation and the host's local add, install, details, fresh invocation, refresh, uninstall and reinstall commands. Verify version, payload and profile signatures, then clean up.

## Completion notes

- Isolated installation, payload comparison, refresh, removal, reinstall and strict validation passed using a temporary home. See `docs/validation.md`.
- After authentication was refreshed, enterprise policy blocked the local marketplace. The user explicitly directed that Claude model checks be skipped. Authenticated installation, invocation and reference loading remain unverified.
