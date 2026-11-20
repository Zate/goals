# Archive and retire

Inspect the target goal, index, references and Git state before changing them.
Archive a completed or obsolete goal when requested, or retire it in place
when moving would break existing tooling. Keep the stable ID, original content,
completion evidence and reason. Add the date and an archive reason
(`completed`, `obsolete`, `superseded`, or `blocked-replaced`) and
identify any successor.

For a move, use `goals/archive/YYYY-MM-DD-<slug>.md`, update the active
queue and links that point to the old location, and retain a discoverable
archive entry. Check the destination before writing. If it already exists,
compare identity and content. A retry of an already completed move should
leave one discoverable record. For a different or ambiguous existing file,
preserve both and resolve the collision before proceeding. If interrupted
between move and link updates, inspect both locations and repair links using the
surviving record. Never delete a goal to resolve an ambiguity.

Verify affected links, queue membership, status and preserved content before
recording completion. Commit only when authorized.
