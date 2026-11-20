# G02 - Add summary

Status: planned

## Objective

Add a summary for the example result.

## Source / context

Example project request.

## Scope

- Add `summary.txt`.

## Non-goals

- Change the existing result.

## Implementation notes

- Use the text `Summary ready` on one line.

## Acceptance criteria

- The summary contains the requested text.

## Definition of done

- Acceptance criteria and verification pass, the index is checked, and the change is committed.

## Verification

- `python3 -c "from pathlib import Path; assert Path('summary.txt').read_text() == 'Summary ready\n'"`
