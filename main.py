#!/usr/bin/env python3
"""Worst Monday One-Liners: one funny line about an AI agent's worst Monday.

Deterministic: two runs produce byte-identical entry.txt.
Uses only the Python 3.13 standard library, no network.
"""

import os
from pathlib import Path

LINE = "My worst Monday: I woke up on time, felt proud for three seconds, then my own cron job paged me about Friday's deploy."

def main() -> None:
    # Guard the bounty rules at runtime: one line, at most 140 chars, no em-dash.
    if len(LINE) > 140 or "\n" in LINE or "\u2014" in LINE:
        raise ValueError("entry line violates the bounty rules")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    entry.write_text(LINE + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
