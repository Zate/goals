# G08 - Verify the Codex install lifecycle

Status: complete

Prerequisites: G07

## Objective

Show that Codex can install, discover, update and remove the local Goals marketplace package.

## Source / context

[Delivery plan](../PLAN.md) M6 and [PRD](../PRD.md) R8.

## Scope

- Run the local smoke in an isolated Codex profile. Return Codex-only evidence for `docs/validation.md`.

## Non-goals

- Normal profile installs and remote marketplace testing.

## Implementation notes

- Use a disposable copy and consumer repo. Record CLI version and source revision. Snapshot normal-profile signatures before and after. Compare installed inventory and hashes. Use a distinct fixture version to exercise refresh.

## Acceptance criteria

- A fresh session discovers one Goals skill and resolves its references from outside the source repo. Refresh exposes the distinct version. Uninstall removes the plugin, and reinstall restores it. Normal profile signatures match.

## Definition of done

- Acceptance criteria pass and verification results are recorded.
- Focused tests or fixture checks and relevant docs reflect the change.
- Status is `complete`, the index row is checked, and the goal has one focused commit.

## Verification

- Run and record the host's local add, install, list, fresh invocation, refresh, uninstall and reinstall commands. Verify package version, payload hashes and normal-profile signatures, then clean up.

## Completion notes

- Isolated installation, inventory, payload comparison, refresh, removal and reinstall passed for version 0.1.0. Normal profile signatures matched. See `docs/validation.md`.
- Authenticated invocation was denied by enterprise-managed requirements for both the checkout and a disposable copy. The user explicitly directed that this check be skipped. Reference loading in a live Codex session is unverified.
