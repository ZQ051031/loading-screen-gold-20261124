#!/usr/bin/env python3
"""Loading Screen Gold entry: one loading-screen tip, at most 200 chars.

Writes the entry line to /output/entry.txt using only the standard library.
"""

import os

ENTRY = "Tip: the bar isn't stuck \u2014 it's just loading your patience, one percent at a time. Go on, blink."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
