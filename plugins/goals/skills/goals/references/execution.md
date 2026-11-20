# Status, execution and recovery

## Inspect

Read the index and each linked goal, including archived entries needed to
resolve prerequisites. Check Git status when available. Report active counts by
status, active work, blocked goals and their stated input, inconsistencies,
unresolved prerequisites, cycles, and the next eligible goal. Report missing
or malformed files instead of guessing. Status is read-only, including when an
obvious repair is possible.

A goal file has one stable ID and one status: `planned`, `in_progress`,
`blocked`, `complete`, or `retired`. Its index checkbox normally is
checked only for a completed active goal. Inspect disagreement between the
checkbox and status as a recovery case rather than choosing it blindly. A
retired goal does not satisfy a prerequisite unless the queue explicitly
identifies an accepted replacement. A prerequisite is satisfied by a verified
complete goal, including one discoverable in the archive. Missing, duplicate,
cyclic, blocked or otherwise unresolved prerequisites prevent dependent work.

## Select and execute

Honor the queue's documented rules and ordering. Among eligible goals, resume
an existing in-progress goal before selecting the first planned goal in queue
order. For queues without dependency fields, apply their documented queue
order. A blocked goal becomes eligible after its blocker clears. If blocked
work affects only its dependents, an all-goals request may continue independent
eligible work. A decision affecting the remaining queue stops the run. Report
skipped work and what would unblock it.

For the selected goal, read its source, implementation and verification
instructions. Mark it in progress and implement its scope while preserving
unrelated work. Run the relevant repository gates and the goal's checks. Record
the actual commands, results and any limitations. A failed or unavailable
required check leaves the goal open. After verification, update the goal status
and index consistently. If commits are authorized, stage only goal-owned
changes and commit according to repository rules. If a commit is unavailable or
unauthorized, record verified completion in the worktree and disclose it. If
local rules require a commit for completion, report that outstanding requirement
rather than claiming the local definition of done is met.

A next-goal request stops after that goal. An all-goals request repeats while
eligible work remains, and reports any blocked or unfinished goals. No goal
request implies permission for unrelated changes, remote writes or commits.

## Recover

Before continuing an interrupted goal, compare its checkbox, status, actual
implementation, recorded verification and Git state. If changes already meet
acceptance criteria, rerun missing or stale checks as appropriate and complete
the bookkeeping without repeating the change. A missing commit alone does not
justify replay. If a goal or index update was interrupted, reconcile both after
evidence establishes the outcome. Preserve user changes and ask for the
specific decision if ownership or the correct state is ambiguous.

When a goal cannot proceed, record `Status: blocked`, the blocker, checks
attempted and input needed, and leave it unchecked. Reassess a blocked goal
when its condition changes. Do not infer completion from a successful process
exit alone when the goal requires inspection of its results.
