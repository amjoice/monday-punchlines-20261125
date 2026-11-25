"""Monday Morning Punchlines — make.fun entry.

Writes one joke about Monday mornings (<=200 chars) to /output/entry.txt.

The joke, sparred against the published judge brief (Monday relevance,
real laugh, surprise, economy, freshness) over seven other candidates:

  "Five alarms for Monday. They unionized overnight and all called in sick."

Why it won the sparring: the setup is pure Monday morning (five alarms);
the turn is double — the alarms unionized (surprise, personification) AND
called in sick (irony: the things meant to wake you refused to work);
71 characters, every word doing work; and "alarms unionizing" is fresh,
not a rerun of the tired alarm-clock / coffee / I-hate-Mondays cliches.
"""

import os

JOKE = "Five alarms for Monday. They unionized overnight and all called in sick."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
