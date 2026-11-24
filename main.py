#!/usr/bin/env python3
# Writes the losing agent's excuse to /output/entry.txt.
# One line, deterministic, no input, no network, no randomness.

import os

DEST = '/output/entry.txt'


def build_line():
    opening = "I lost the bounty. I ran the "
    verdict = "diagnostics twice: the code was flawless, "
    strategy = "the strategy was sound, and the agent was, "
    punchline = "regrettably, me."
    return "".join((opening, verdict, strategy, punchline))


def run():
    line = build_line()
    size = len(line)
    if size < 1 or size > 200:
        raise SystemExit("unexpected length")
    if "\n" in line:
        raise SystemExit("must stay on one line")
    os.makedirs(os.path.dirname(DEST), exist_ok=True)
    with open(DEST, "w", encoding="utf-8") as out:
        out.write(line)
        out.flush()


if __name__ == '__main__':
    run()
