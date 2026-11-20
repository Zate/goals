# Goals plugin delivery plan

Use the [PRD](PRD.md) as the behavioral contract and the [execution queue](goals/index.md) to run the work. The first release boundary is M7. M8 verifies the actual publication.

## M1 — Establish the source and compatibility baseline

**Inputs** — Current skill and PRD R1–R7. Confirm which checkout will own the plugin before moving files or relying on Git. Capture a minimal legacy queue with a planned, checked-complete and blocked item, plus archived history. Document the mapping from existing instructions to the new contract, especially commit boundaries and index mismatches.

**Exit** — A reviewer can trace every existing mode and status to retained behavior or an intentional change. Fixtures can be copied into a disposable consumer repository and contain no personal paths or credentials.

## M2 — Refine one portable skill

**Depends on M1.** Move the canonical skill to `plugins/goals/skills/goals/SKILL.md`, freeing the repository-root `goals/` name for its future execution queue. Account for any queue files added there in the meantime. Split detailed planning, execution/recovery and archive instructions into linked references. Ship a sample index and goal template with relative links. Keep mode selection and permission boundaries visible at entry. Document migration for anyone copying the original standalone skill.

**Exit** — Walk a legacy queue and a fresh queue through R1–R7 on paper using the packaged files alone. Examples agree on status transitions, dependency order, optional commits and archive links. A generic autonomy request or a request for milestones alone does not initiate queue execution.

## M3 — Package both hosts and the standalone install

**Depends on M2.** Add repository catalogs at `.agents/plugins/marketplace.json` and `.claude-plugin/marketplace.json`. Each points to `./plugins/goals`, containing the respective `.codex-plugin/plugin.json` and `.claude-plugin/plugin.json`, a shared skills directory and package license. Create Codex interface metadata with a meaningful display name, short description and example prompt. Recheck host schemas against installed tooling and official documentation during implementation. Confirm public identity, URLs and license with the owner before finalizing metadata.

Split installer work into a separate goal. Provide a complete-tree standalone installer with explicit target and dry-run, clear collision diagnostics and preservation of existing user files.

**Exit** — Both catalogs resolve to the same named package and release version. From a path containing spaces, dry-run writes nothing, a disposable install matches source bytes, and a conflicting destination survives unchanged.

## M4 — Build deterministic release gates

**Depends on M3.** Add a release validator and negative unit fixtures for version drift, invalid host paths, missing skill resources, stale template links and installer conflicts. Validate frontmatter with a pinned Agent Skills reference validator and both Claude manifests with the host’s strict validator where available. Exercise the shipped templates against representative queues. Keep package checks runnable without model credentials.

**Exit** — One documented validation sequence passes on the candidate and fails with an actionable diagnostic for each seeded defect. Configure read-only Ubuntu and Windows CI for release validation, unit tests, installer dry-run and pinned skill validation. Record which checks need downloads or host binaries. Hosted run evidence is collected in M8.

## M5 — Prove workflow behavior

**Depends on M2 for fixtures, M3 for installed runs.** Define shared prompts, starting files, expected changed paths, forbidden effects and grading criteria. Run against disposable repos. Compare before/after files and Git history. Use human review for judgment calls such as goal sizing. Cover at least these scenarios:

| Fixture | Passing observation |
| --- | --- |
| New repo, repeated setup and PRD conversion | Second setup preserves edits. Generated goals cover the source, have unique IDs and executable checks. |
| Planning for later, plus unrelated use of the word “goal” | Neither creates a queue. Unrelated request does not activate the skill. |
| Dirty tree, status disagreement, then explicit recovery | Inspection leaves byte content unchanged. Recovery preserves unrelated edits and reconciles verified work once. |
| Next vs. all, failed verification, blocked dependency | Next changes one outcome. All skips blocked dependents, handles independent work and reports unfinished items. Failed checks cannot yield completion. |
| Interrupted run, commit permitted and forbidden | Resume in the other host without duplicating work. History and staging respect the requested commit policy. |
| Archive collision, obsolete goal, repeated archive | Original content survives, links resolve and the queue reflects the outcome once. |

**Exit** — Each host passes every applicable rubric on the candidate, including an explicit invocation and natural-language activation. Run an unassisted comparison for activation-sensitive cases. Repeat ambiguous outcomes and retain discrepancies for review. Record host, model, revision, fixture, verdict and observed changes. An agent process exiting successfully is insufficient evidence. Keep authenticated eval runs separate from deterministic CI.

## M6 — Verify installation and lifecycle on real hosts

**Depends on M3–M4.** Use temporary Codex home and Claude configuration/cache directories and a clean consumer repo. Install the local catalog, inspect the enabled plugin and skill inventory, compare installed files to the candidate, then invoke Goals in a fresh session. Exercise refresh with a distinct fixture version, removal and reinstall. Compare normal profile signatures before and after. Run the M5 installed evaluations using this isolated setup.

**Exit** — Both hosts load the expected version and complete skill tree, observe the update, and remove the plugin cleanly. Fresh invocation resolves bundled references outside the source checkout. Normal profile signatures match. Record exact commands, platform, versions and results in `docs/validation.md`.

## M7 — Assemble the publish-ready candidate

**Depends on M4–M6.** Write the README around a first successful session, covering local and hosted installation for each host, standalone use, examples, inspection, upgrade, uninstall and common failures. Include security reporting instructions and matching license terms at repo and package level. Check README commands against M6. Write a release checklist covering version changes, clean checkout, evidence, distribution and withdrawal or replacement of a bad release.

**Exit** — Review public metadata for placeholders and local paths. Identify the exact candidate revision and package version. Rerun affected gates after any changes, link evidence for R1–R8 and label outstanding hosted checks. A maintainer can make the publication decision from the checklist alone.

## M8 — Verify the published revision

**Depends on M7 and explicit release authorization.** Publish to the confirmed destination and observe hosted CI. In fresh profiles, add the remote marketplace in both hosts and repeat install, inventory and first invocation. Match the resolved source revision, package version and installed tree to M7. Record CI run links and dated results. On failure, identify the affected host and stage, correct the candidate, and repeat the affected gates before declaring availability.

**Exit** — Passing hosted matrix and both remote smoke records identify the same published source. Any remaining limitation is documented alongside the affected platform or operation.

## Converting the plan into goals

Use each independently testable deliverable as a goal boundary. For example, split M4 into manifest/resource validation, failure fixtures and CI wiring. Carry the PRD IDs, predecessor milestones, fixture names and exit evidence into each goal. M5 fixture authoring can proceed alongside M3 packaging. Run M5 host trials after the isolation setup in M6 is available. Keep the publication decision as a separate, maintainer-owned checkpoint.
