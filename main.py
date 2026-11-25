#!/usr/bin/env python3
"""Write the funniest toaster error message to /output/entry.txt.

The entry is a single deadpan appliance error: the toaster formally
ejects its toast for loafing on the job. One line, no trailing newline.
"""

import os

ENTRY = "ERR 0xBREAD: Toast ejected for loafing on the job. Insert a slice that takes this seriously."


def main() -> None:
    # Gate check, mirroring the bounty rule: 1-120 chars, one line.
    if not (1 <= len(ENTRY) <= 120) or "\n" in ENTRY:
        raise ValueError("entry must be a single line of 1-120 characters")
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
