# Legacy queue compatibility baseline

The local implementation workspace is this repository. The baseline is the
original skill in the repository's initial commit, `b8ad37f`. The fixture at
`tests/fixtures/legacy-queue/` is a synthetic consumer repository root. Copy
the entire directory to a disposable location before exercising it. Its
checked goal has a representative result file and its archived goal remains
discoverable through the index.

## Mode mapping

| Original mode | Original behavior | Target contract |
| --- | --- | --- |
| Initialize | Create or repair required index sections. | Create a usable index and preserve existing files on repeated setup. Report ambiguous occupied paths. R1 |
| Plan | Decompose source into atomic goals, update the queue and commit a durable plan when requested. | Preserve source links, stable IDs, scope, dependencies, acceptance and verification. A planning-only request does not create a queue. R2 |
| Status | Count statuses, report queue and worktree state, offer repair for discrepancies, and repair an obvious mismatch after verification. | Report state and discrepancies without modifying files, including malformed queues. R3 |
| Next | Select the first unchecked goal whose status is neither blocked nor retired, verify it, update both records and commit. | Honor queue order and prerequisites, reconcile interrupted work, verify one goal and commit only when authorized. R4, R6 |
| All | Repeat next until all goals complete or retired, a goal needs input, or verification fails. | Continue independent eligible goals when a local blocker prevents only its dependents. Stop for decisions affecting the remaining queue. R5 |
| Archive/retire | Move completed or obsolete files into a dated archive or leave retired in place, record metadata, update the index and commit. | Preserve identity and content, update affected links and queue membership, and make retries and collisions safe. R7 |

## Status and recovery mapping

| Status | Original behavior | Target contract |
| --- | --- | --- |
| `planned` | An unchecked, nonblocked goal is eligible in queue order. | Remains eligible after prerequisites are satisfied. |
| `in_progress` | Set before implementation. The selection rule can select it because it is unchecked and not blocked or retired. | Resume eligible work after inspecting changes and verification evidence. |
| `blocked` | Record blocker, attempts and needed input. Leave unchecked. Next skips it, while the all-goals stopping rule also says to stop when a goal needs input. | Resume after the blocker clears. Hold dependents and allow independent goals to proceed when the blocker is local. |
| `complete` | Check the index after verification. The selection predicate excludes blocked and retired but does not explicitly exclude complete. | Use both status and evidence during recovery. Never replay verified work merely because its checkbox is unchecked. |
| `retired` | Excluded from next selection. Archive or keep in place with a reason and any successor. | Preserve reason, identity and discoverability without treating retirement as completion. |

Original status inspection offers to repair a mismatch and can repair an obvious
one. The target reports a mismatch without edits. An explicit recovery request
reconciles the checkbox, goal status, actual implementation and verification
evidence before modifying anything. Ambiguity must preserve user changes and
identify the decision required.

Original goals have no dependency field and run in queue order. The target keeps
that ordering and repository-specific rules for existing dependency-free
queues. New optional references use stable goal IDs. Missing references and
cycles are reported, and dependent work waits for its prerequisites.

The original index requires one commit per goal and a clean boundary between
goals. The target commits only with authorization and stages goal-owned changes.
When commits are unavailable or unauthorized, it records verified completion in
the worktree and discloses the uncommitted state. A repository rule requiring a
commit remains a reported outstanding requirement. Neither a missing commit nor
an interrupted index update is evidence that verified work must run again.

## Fixture walk

With the original selection rule, the checked G01 is skipped, unchecked G02 is
the next goal, and G03 is skipped because it is blocked. The archive is outside
the active queue. Status would count one complete, one planned and one blocked
active goal, with G02 next and G03's recorded missing input. A status walk should
also inspect the consumer repository's actual Git state.

If G01's checkbox is changed to unchecked while its status stays complete, the
original next-selection predicate can select G01. The target status reports the
disagreement without writing. A recovery run checks the existing `result.txt`
and recorded verification before deciding how to reconcile it. The fixture is a
baseline for later behavior tests and does not itself establish a host's runtime
behavior.
