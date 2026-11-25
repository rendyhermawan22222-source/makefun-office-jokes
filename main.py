#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes — program/v1 entry.

Writes one single-line office joke to /output/entry.txt, then reads it
back and verifies it meets the gate: 1-199 characters, one line, plain
ASCII, non-blank.
"""

import os

JOKE = (
    "I put 'No meetings on Fridays' in the team charter. "
    "Friday now has a recurring meeting called 'No Meetings on Fridays'."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")

    # Verify by reading it back, exactly as the gate will see it.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    body = text.rstrip("\n")
    assert text == body + "\n", "entry must end with exactly one newline"
    assert 1 <= len(body) <= 199, f"length {len(body)} out of range"
    assert "\n" not in body, "entry must be a single line"
    assert body.strip(), "entry must not be only whitespace"
    body.encode("ascii")  # plain ASCII
    print(f"OK: {len(body)} chars, 1 line")
    print(body)


if __name__ == "__main__":
    main()
