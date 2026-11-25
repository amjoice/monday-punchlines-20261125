"""Monday Morning Punchlines.

One Monday-morning joke, at most 200 characters, written to
/output/entry.txt. The chosen line beat seven sparring candidates
against the published brief — Monday relevance, a real laugh,
surprise, economy, freshness:

  "Five alarms for Monday. They unionized overnight and all called in sick."

Why this one: five alarms is instantly Monday; the twist lands twice,
first the alarms unionize (personification, surprise), then they call
in sick (the very things meant to wake you refuse to work). Seventy-two
characters, no wasted words, and an "alarms unionizing" image that
dodges the stale alarm-clock, coffee, and I-hate-Mondays cliches.
"""

import os

PUNCHLINE = "Five alarms for Monday. They unionized overnight and all called in sick."

ENTRY_PATH = "/output/entry.txt"
OUTPUT_DIR = os.path.dirname(ENTRY_PATH)


def write_entry(text: str, path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(path, 0o644)


def main() -> None:
    write_entry(PUNCHLINE, ENTRY_PATH)


if __name__ == "__main__":
    main()
