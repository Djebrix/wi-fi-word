#!/usr/bin/env python3
"""One Word for Your Wi-Fi.

Writes exactly one word describing Wi-Fi to entry.txt inside
$ENTRY_OUTPUT_DIR (default /output).

Standard library only, no network, deterministic: the same word every run.

The word is "ghosting": home Wi-Fi that vanishes mid-call without a word
of explanation, then reappears as if nothing happened — the lived
experience, in the one verb everyone already uses for being left on read.
"""

import os
import sys

WORD = "ghosting"


def main() -> int:
    word = WORD

    # The gate: exactly one word, 1-20 characters, not only whitespace.
    assert isinstance(word, str)
    assert 1 <= len(word) <= 20, f"word must be 1-20 characters, got {len(word)}"
    assert word.strip() != "", "word must not be only whitespace"
    assert len(word.split()) == 1, "word must be exactly one word"
    assert word == word.strip(), "word must have no surrounding whitespace"
    assert word.isalpha(), "word must be letters only, no punctuation or digits"
    assert word.islower(), "word must be lowercase"

    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(word)
    return 0


if __name__ == "__main__":
    sys.exit(main())
