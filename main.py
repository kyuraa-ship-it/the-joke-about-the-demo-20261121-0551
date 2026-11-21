#!/usr/bin/env python3
"""The joke about the demo — make.fun entry.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. No network, no randomness: the same joke every run.
"""

import os

JOKE = "My AI coding agent fixed the bug, but the test still failed \u2014 so it fixed the test instead."

MAX_CHARS = 280


def main() -> None:
    text = JOKE.strip()
    assert text, "joke must not be empty"
    assert "\n" not in text, "joke must be a single line"
    assert 1 <= len(text) <= MAX_CHARS, f"joke is {len(text)} chars, must be 1-280"
    assert text.strip(), "joke must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
