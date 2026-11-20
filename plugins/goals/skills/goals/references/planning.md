# Initialize and plan

Inspect repository instructions, existing planning material, the target
`goals/` path and its index before writing. Create a usable index when absent.
If an existing path or partial index is ambiguous, report what is there and
resolve the conflict before changing it. Repeating setup preserves existing
goals, instructions and edits. Do not silently normalize a legacy index.

Use [the index example](../assets/index.md) and
[goal example](../assets/goal.md) as adaptable starting points. Replace
placeholders and select verification commands that actually apply to the
consumer repository. Include its execution rules and verification in its index
so another agent can resume from that index and its linked files.

For an explicit request to turn a PRD or other source into goals:

1. Read the source and relevant repository context. Identify independently
   verifiable outcomes and split work that cannot be completed and checked as
   one coherent change. Preserve source references and local constraints.
2. Assign unique stable IDs without renumbering existing goals. Record the
   objective, source, scope, non-goals, acceptance criteria, verification and
   status in each file. Add links in queue order.
3. Record real dependencies using `Prerequisites: G01, G02`, or
   `Prerequisites: None`. Resolve references against IDs in the active and
   archived index. Report duplicates, missing IDs and cycles. Do not invent
   dependencies merely to serialize independent work.
4. Check links, coverage of the source, scope, dependency order and testability.
   Record any checks that cannot run. Commit only when authorized.

A queue without prerequisite fields follows its existing documented order and
rules. Do not add fields or alter historical goal files just to adopt this
format. A request for a PRD or milestones for later conversion produces those
requested artifacts without initializing a queue.

## Standalone migration

Previous standalone users may have copied only the old `goals/SKILL.md`.
Install or copy the entire new `goals` skill directory, including
`references/` and `assets/`, into the host's skill location. Remove an old
standalone copy only with the owner's authorization. Existing consumer
`goals/index.md` and goal files remain in place and are read as legacy queues.
