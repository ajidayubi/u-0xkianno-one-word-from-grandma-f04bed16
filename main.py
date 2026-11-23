#!/usr/bin/env python3
"""One Word From Grandma: write the single word a grandma would text about AI.

The word is the classic grandma typo for "robot": warm, a little baffled,
instantly readable, and funny on its own with no caption. Writes exactly
that one word (5 characters, no trailing newline) to /output/entry.txt,
atomically, so the file is never left half-written.
"""
import os

WORD = "Robit"
OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    tmp_path = OUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(WORD)
    os.replace(tmp_path, OUT_PATH)


if __name__ == "__main__":
    main()
