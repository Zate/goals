# G04 - Build the standalone installer

Status: planned

Prerequisites: G02

## Objective

Install the complete shared skill tree safely into an explicit standalone target.

## Source / context

[Delivery plan](../PLAN.md) M3 and [PRD](../PRD.md) R8.

## Scope

- Own `scripts/install_agent_skills.py` and its focused tests. Support dry-run, explicit destination and actionable collision diagnostics.

## Non-goals

- Host marketplace commands, updates of an existing installation and global installs.

## Implementation notes

- Resolve the source relative to the script. Copy the whole tree, including references, templates and metadata. Preserve existing data on conflict or a partial failure. Use fixtures for paths with spaces and platform-sensitive path handling.

## Acceptance criteria

- Dry-run reports the install paths without writing. A fresh install matches the source tree byte for byte. An existing destination survives a conflicting install unchanged.

## Definition of done

- Acceptance criteria pass and verification results are recorded.
- Focused tests or fixture checks and relevant docs reflect the change.
- Status is `complete`, the index row is checked, and the goal has one focused commit.

## Verification

- Run `python3 -B -m unittest discover -s tests -p 'test_install_agent_skills.py' -v`. Exercise dry-run, a successful disposable install, a destination containing spaces and an existing destination. Compare filenames and hashes.
