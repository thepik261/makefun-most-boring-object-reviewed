#!/usr/bin/env python3
"""Entry for make.fun bounty: The Most Boring Object, Reviewed in One Line.

Writes one funny, true, single-line review (<= 200 characters) of a boring
everyday object to /output/entry.txt. Pure Python standard library only;
fully deterministic — the same line every run.
"""

import os

ENTRY = (
    "The doorstop has held this door open for six years without one "
    "thank-you, and the day it goes missing, everyone blames the wind."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = ENTRY.strip()
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    assert "\n" not in line, "entry must be a single line"
    # The file holds the line plus one trailing newline (129 bytes total),
    # still well inside the 1-200 character gate.
    out_dir = os.path.dirname(OUTPUT_PATH)
    os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    # Make the created file readable by every user (the grader collects
    # outputs as a different user). Never chmod /output itself.
    try:
        os.chmod(OUTPUT_PATH, 0o644)
    except OSError:
        pass


if __name__ == "__main__":
    main()
