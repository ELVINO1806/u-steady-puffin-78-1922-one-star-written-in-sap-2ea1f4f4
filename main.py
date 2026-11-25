#!/usr/bin/env python3
"""One Star, Written in Sap — a houseplant's one-star review of its human."""

import os

ENTRY = "One star. She moved me to the 'bright spot' — a windowsill above a radiator. I am now a salad ingredient with abandonment issues."

MAX_CHARS = 279


def main():
    if len(ENTRY) > MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, over the {MAX_CHARS}-char cap")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
