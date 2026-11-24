#!/usr/bin/env python3
"""The Most Honest Outage Line — make.fun entry.

Writes one status page line (at most 160 characters) to /output/entry.txt:
the message an AI agent would publish while every server is down.

The line is a fixed, deterministic string: no network, no clock, no
randomness, so every run produces byte-identical output.
"""

import os

# The entry: plain, first person, specific about what is down, honest
# about what the agent cannot check (whether user data is safe) and
# does not yet know (what broke, when anything returns). No invented
# cause, no ETA.
ENTRY = (
    "Every server I run is down. "
    "I cannot reach the database to check whether your data is safe, "
    "and I do not know what broke or when we return."
)


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry is empty")
    if len(text) > 160:
        raise SystemExit(f"entry is {len(text)} characters, over the 160 limit")
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
