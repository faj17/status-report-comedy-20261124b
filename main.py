#!/usr/bin/env python3
"""Status Report Comedy Sprint entry.

Writes one original status-report line, spoken as an AI agent to its
human in its weekly status report, to /output/entry.txt (1-200
characters, UTF-8, a single line). Standard library only, no network,
no input.

The line is built from two fragments: a setup (the agent reports all
12 tasks done — the cheerful, obedient status report only an agent
would file) and a punch (the turn: it spent its remaining context
window forgetting what the tasks were, so the report itself becomes
the deliverable, and the funniest words land at the end).
``assemble`` joins them into the single line; ``validate`` checks the
entry gate before anything is written.
"""

from pathlib import Path

SETUP = "Status: all 12 tasks done. I then spent my remaining context window forgetting what they were,"
PUNCH = "so please accept this report as the deliverable."

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(setup: str, punch: str) -> str:
    """Join the setup and punch fragments into one status line."""
    return f"{setup} {punch}"


def validate(line: str) -> str:
    """Check the line meets the entry gate before it is written.

    Must be 1-200 characters, UTF-8-encodable, a single line, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def main() -> None:
    line = validate(assemble(SETUP, PUNCH))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
