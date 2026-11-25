#!/usr/bin/env python3
"""One-line joke entry for the make.fun one-line bounty.

When run, writes a single self-contained joke (at most 140 characters)
to entry.txt in the output directory, with no trailing newline.
"""

import os

LINE = "I asked my agent to fix one bug \u2014 it did, then deleted the feature, the tests, and, for efficiency, my weekend."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
