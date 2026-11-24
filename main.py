#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single absurd invention pitch (one sentence, max 220 chars)
to /output/entry.txt. Stdlib only, no network, deterministic.
"""

import os

ENTRY_TEXT = (
    "A context window for your houseplants: it remembers where you left "
    "the watering can, so your fern finally stops dying of your amnesia."
)

MAX_CHARS = 220


def main() -> None:
    text = ENTRY_TEXT

    # Gate, mirroring the sealed scorer: UTF-8 text, 1-220 chars,
    # not only whitespace, exactly one sentence, no trailing newline.
    if not text or text != text.strip() or not text.strip():
        raise SystemExit("entry text must be non-empty, non-whitespace text")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry text is {len(text)} chars, over the 220 limit")
    if not text.endswith("."):
        raise SystemExit("entry text must end with a single full stop")
    body = text[:-1]
    if "." in body or "!" in body or "?" in body:
        raise SystemExit("entry text must be exactly one sentence")

    os.makedirs("/output", exist_ok=True)
    out_path = "/output/entry.txt"
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    # Best-effort readability on the entry file ONLY. Never chmod /output
    # itself: the grader runs as a different uid and chmod on the directory
    # fails with EPERM.
    try:
        os.chmod(out_path, 0o644)
    except OSError:
        pass


if __name__ == "__main__":
    main()
