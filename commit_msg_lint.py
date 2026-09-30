#!/usr/bin/env python3
"""Lint a git commit message from a file or stdin."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

CONVENTIONAL_TYPES = {
    "feat",
    "fix",
    "docs",
    "style",
    "refactor",
    "test",
    "chore",
}


def read_message(path: str | None) -> str:
    if path:
        return Path(path).read_text(encoding="utf-8")
    return sys.stdin.read()


def subject_line(message: str) -> str:
    for line in message.splitlines():
        if line.startswith("#"):
            continue
        return line.strip()
    return ""


def lint(message: str) -> list[str]:
    errors: list[str] = []
    subject = subject_line(message)
    if not subject:
        errors.append("Commit subject is empty.")
        return errors

    if ":" in subject:
        prefix = subject.split(":", 1)[0]
        kind = prefix.split("(", 1)[0]
        if kind not in CONVENTIONAL_TYPES:
            errors.append(
                f"Unknown type '{kind}'. Use one of: {', '.join(sorted(CONVENTIONAL_TYPES))}."
            )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint a git commit message.")
    parser.add_argument("path", nargs="?", help="Path to COMMIT_EDITMSG or a text file")
    args = parser.parse_args()

    message = read_message(args.path)
    errors = lint(message)
    if errors:
        for error in errors:
            print(error)
        return 1
    print("Commit message looks good.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
