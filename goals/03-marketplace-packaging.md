# G03 - Package the two marketplaces

Status: complete

Prerequisites: G02

## Objective

Make one Goals payload discoverable by both local marketplaces.

## Source / context

[Delivery plan](../PLAN.md) M3 and [PRD](../PRD.md) R8.

## Scope

- Own the root catalogs at `.agents/plugins/marketplace.json` and `.claude-plugin/marketplace.json`, and manifests under `plugins/goals/.codex-plugin/` and `plugins/goals/.claude-plugin/`. Add Codex presentation metadata, including the skill’s `agents/openai.yaml`.

## Non-goals

- Standalone installer, host lifecycle, and publication.

## Implementation notes

- Use `goals` and `goals-marketplace` as proposed public names. Check current host schemas against official documentation and installed tooling. Use verifiable local metadata and defer unconfirmed optional public values and license to G11.

## Acceptance criteria

- Both catalogs resolve to the same package path, identity and version. Both manifests expose the same one-skill tree. Codex display and example prompts describe the actual product.

## Definition of done

- Acceptance criteria pass and verification results are recorded.
- Focused tests or fixture checks and relevant docs reflect the change.
- Status is `complete`, the index row is checked, and the goal has one focused commit.

## Verification

- Parse every JSON manifest and resolve package and skill paths. Run Claude's strict manifest checks against both roots using the verified CLI syntax when available. Record any unavailable host check for G09.

## Completion notes

- Both Claude strict manifest validations passed with no manifest warnings or errors. JSON identity, version, source paths and single-skill inventory checks passed. The directory report flags README and license work covered by G11, plus an optional directory icon.
- `Goals Contributors` is a provisional project attribution pending G11 review. Local host installation is covered by G08 and G09.
