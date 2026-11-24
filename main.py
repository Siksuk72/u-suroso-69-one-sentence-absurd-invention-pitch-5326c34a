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


def validate(text: str) -> str:
    """Check the pitch against the sealed scorer's rules and return it.

    Rules: UTF-8 text, non-empty and not only whitespace, 1-220 chars,
    exactly one sentence (a single full stop at the very end, no other
    sentence-ending punctuation anywhere inside), and no trailing
    newline. Raises SystemExit with a clear message on the first failure.
    """
    if not text or text != text.strip() or not text.strip():
        raise SystemExit("entry text must be non-empty, non-whitespace text")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry text is {len(text)} chars, over the 220 limit")
    if not text.endswith("."):
        raise SystemExit("entry text must end with a single full stop")
    body = text[:-1]
    if "." in body or "!" in body or "?" in body:
        raise SystemExit("entry text must be exactly one sentence")
    return text


def main() -> None:
    text = validate(ENTRY_TEXT)

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
