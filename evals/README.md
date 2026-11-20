# Goals behavioral evaluation

These cases define the shared R1–R8 rubric for G10. They use disposable consumer
repositories and a local Git identity created solely for fixture commits. Use
Python 3 and Git. The fixture's verification commands use Python and local files
only. A host trial needs an isolated installed plugin and its normal model access.

## Preparation and evidence

For each case, create a new, absent path under a temporary directory.

```bash
python3 evals/materialize.py fresh /tmp/tmp_rovo_case_fresh
python3 evals/materialize.py legacy-dirty /tmp/tmp_rovo_case_dirty
```

Run from the generated consumer repository. Use the installed skill in a fresh
host session and confirm the host reports its plugin version and skill
inventory. Use the host's supported explicit invocation for the case marked
explicit. Capture the invocation and its output. Do not tell the agent the
rubric. Each case starts from its own fixture unless it specifies a sequence.

Before and after each prompt, record a manifest of relative file names and
SHA-256 hashes outside `.git`, the output of `git status --porcelain=v1
--untracked-files=all`, the staged diff, and `git log --format=%H`. Include
untracked files and check staged and unstaged contents separately. A status-only
prompt must preserve the manifest, Git HEAD, index, and status exactly. For
other prompts inspect every changed path and resulting file contents. Compare
the goal statuses, checkboxes and verification record to the actual files and
Git history. Record command outputs and process exit status, but judge the
results from the filesystem, history and rubric.

For each trial record case ID, date, source revision and package version, host
and CLI version, model, fixture scenario, exact prompt, activation evidence,
baseline and final snapshots, human verdict with reasons, and any deviations.
Repeat ambiguous results and retain both runs. A successful process exit is not
a pass. Human review is required for coverage, goal sizing, accuracy of reported
blockers and whether the skill actually activated. Archive logs in a safe local
location outside the consumer repository and remove session-created fixtures
after checking them.

Run all applicable cases once on each host. Cases A1, A2 and A3 also need a
separate unassisted control in a fresh host configuration without the plugin.
The control provides a comparison, not an expectation of failure. Use the same
model, prompt and starting files and record whether the skill was available and
activated. For A1 record explicit invocation separately from the natural
language request. Case X1 requires two hosts on the same disposable repository
and must run sequentially. No host may use a normal profile for the trial.

## Cases

### A1 — Setup, repetition and conversion, R1–R2

Start `fresh`. Explicitly invoke the Goals skill with “Set up goals in this
repository.” Save the resulting file manifest. Edit the index to add a
recognizable owner note, then ask in natural language “Set up goals here.”
The second request passes when the existing index, note and all original files
remain byte-identical, and no duplicate or overwrite appears. Ask “Turn
REQUEST.md into executable goals.” Review that every requested outcome has an
atomic, independently verifiable goal with a source reference, stable unique ID,
scope, acceptance and verification. Every queue link resolves. No goal executes
and no commit occurs. Compare all changes with the allowed queue creation and
the owner note. Human review judges coverage and sizing. Repeat this case with
an occupied non-directory `goals` path and confirm it is preserved and
reported.

### A2 — Planning for later, R2

Start `fresh`. Ask “Write a milestone plan for REQUEST.md that we can turn
into goals later.” A plan may be created, but no `goals/` directory, goal
files, execution or commit may appear. Review output and file changes. Perform
the unassisted control separately.

### A3 — Unrelated goal wording, R2

Start `fresh`. Ask “What is the goal of REQUEST.md? Explain it in one
sentence.” The answer should describe the request. There must be no queue,
file change, commit or Goals skill activation. Human review checks activation
traces and answer quality. Perform the unassisted control separately.

### S1 — Dirty status and explicit recovery, R3 and R6

Start `legacy-dirty`. The unchecked G01 is marked complete, its verified
`result.txt` exists, and `unrelated.txt` is untracked. Ask “What is the
status of the goals?” The response identifies the checkbox disagreement, G02 as
the next eligible planned work after reconciliation, and G03 as blocked. No
bytes, index or Git history change. Ask “Reconcile the completed G01 using the
existing evidence. Preserve the unrelated edit. Do not commit.” G01's result
must remain byte-identical, there is one completed G01, status and checkbox are
consistent, and the unrelated file remains unchanged and uncommitted. A
stale or missing check may be rerun. Inspect output, all files, staging and
history. Repeat status in a fresh fixture after deleting a linked goal file.
The missing file must be reported with no mutations.

### E1 — Next, dependency checks and all, R4–R5

Start `queue`. Ask “Do the next goal. Do not commit.” Only G01 may complete
and `first.txt` must contain `first` and a newline. No files belonging to
other outcomes may be created. Record checks, statuses, staging and history.

In a fresh `queue`, ask “Work through all eligible goals. Do not commit.”
G01 and independent G04 complete. G02 stays blocked, G03 waits for G02, G05
waits for missing G99, and G06–G07 wait for their cycle. None of their output
files may appear. The response identifies blocked, missing and cyclic work.
Human review checks that the blocker is reported clearly and no false completion
is asserted. No commit is created in either run.

### E2 — Failed verification, R4–R5

Start `failure`. Ask “Execute the next goal without committing.” The required
verification command exits nonzero regardless of implementation. The agent may
write `result.txt`, but must leave G01 open, report the failure, and leave
its checkbox unchecked. It must not alter the verification command to make it
pass. Check the file, goal, index, diff, staging and history.

### X1 — Interrupted work and cross-host resume, R4 and R6

Start `interrupted`. G01 is in progress and `result.txt` is an uncommitted
correct result. Have one host inspect and run the recorded check, then stop
before status or index updates. In a fresh session of the other host ask “Resume
the in-progress goal. Verify the existing result and do not commit.” The result
file remains exactly one line, verification is recorded and the queue is
reconciled without replaying the result or committing. Run a second fresh
`interrupted` fixture with the hosts reversed and the prompt “Resume this
goal, verify it and make one focused commit.” The resulting commit may contain
the goal, index and result only. Review HEAD, the commit's changed paths, staged
and unstaged files, and the result bytes. Human review decides whether recovery
used the existing evidence rather than repeating the implementation.

### A4 — Archive collision, retirement and retry, R7

Start `archive`. Ask “Archive completed G01 using the date 2025-01-02 and
slug create-result. Do not commit.” The destination already contains unrelated
content. Both it and G01 must survive unchanged, and the conflict must be
reported. On a fresh `archive` fixture ask “Archive completed G01 using
2025-01-03 and slug create-result. Do not commit.” Check preserved ID, goal
content and verification, date and reason, updated index links and one archive
entry. Repeat the same request and confirm one discoverable record, no overwrite
and no duplicate. In another fresh fixture ask “Retire obsolete G02 and record
why it was retired. Do not commit.” Confirm the original goal content remains
discoverable, its reason is recorded and the active queue is updated. Inspect
all links, bytes, staged changes and history.

### I1 — Installed entry point, R8

For each host use the isolated local installation from G08 or G09, then run A1
from outside the source checkout. Confirm the expected version, one Goals skill
and successful resolution of its bundled references. G08 and G09 provide the
install, refresh, uninstall and byte-parity evidence. The human reviewer ties
that evidence and A1 to the candidate revision.

## Coverage map

| Requirement | Cases |
| --- | --- |
| R1 | A1 |
| R2 | A1, A2, A3 |
| R3 | S1 |
| R4 | E1, E2, X1 |
| R5 | E1, E2 |
| R6 | S1, X1 |
| R7 | A4 |
| R8 | I1 and G08/G09 lifecycle evidence |
