# G01 - Create result

Status: complete

## Objective

Create the example result.

## Source / context

Example project request.

## Scope

- Add `result.txt`.

## Non-goals

- Add a summary.

## Implementation notes

- Use a single line of text.

## Acceptance criteria

- The file contains `Example result`.

## Definition of done

- Acceptance criteria and verification pass, the index is checked, and the change is committed.

## Verification

- `python3 -c "from pathlib import Path; assert Path('result.txt').read_text() == 'Example result\n'"`

## Completion notes

- Verification: the command above passed when the example was completed.
