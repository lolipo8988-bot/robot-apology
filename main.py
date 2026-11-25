#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Write the entry for 'The Robot Apology' to /output/entry.txt.

The competition asks for one short text of exactly two lines: line
one is a single sentence in which a robot apologizes for one specific
mistake it made, and line two is a single sentence saying what it
learned and what it will do differently, with the lesson following
from that exact mistake. The gate checks that the file is UTF-8 text
of 1 to 400 characters and not only white space.

This program is deterministic: every run writes exactly the same
bytes, and it re-reads the file after writing to prove the bytes on
disk are the bytes intended.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 400

# The apology, revised after the first run. The draft's mistake was
# concrete but its telling was flat: no consequence, and the lesson
# sat close to a generic promise. The final text keeps the same slip
# -- a household robot that trusted the word 'water' on its task list
# and poured from the descaling kettle -- and adds the lived result
# in the machine's own rueful voice: since Tuesday the plant has
# leaned away from its lamp. The lesson is the exact inverse of the
# slip: a label is not the liquid, so read the full contents before
# pouring anything onto something alive.
ENTRY = (
    "I'm sorry: I watered your tomato plant from the descaling kettle, "
    "because my task list said 'water' and I never checked what was "
    "actually inside \u2014 and since Tuesday it has leaned away from my lamp.\n"
    "I learned that a label is not the liquid; from now on I will read "
    "a container's full contents before I pour anything onto something alive."
)


def render() -> str:
    """Return the entry text, checked against the gate's contract."""
    assert 1 <= len(ENTRY) <= MAX_CHARS, (
        f"entry must be 1..{MAX_CHARS} characters, got {len(ENTRY)}"
    )
    lines = ENTRY.split("\n")
    assert len(lines) == 2, f"entry must be exactly two lines, got {len(lines)}"
    assert all(line.strip() for line in lines), "no line may be blank"
    assert ENTRY == ENTRY.strip(), "no leading or trailing white space"
    return ENTRY


def main() -> None:
    text = render()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", os.path.dirname(OUTPUT_PATH))
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, encoding="utf-8", newline="") as f:
        assert f.read() == text, "written entry does not match the intended text"


if __name__ == "__main__":
    main()
