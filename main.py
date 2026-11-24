#!/usr/bin/env python3
"""Write one short dad joke for make.fun bounty u-mfnakmal-dad-joke-showdown-1d2ce3e5."""

import os
import sys

TEXT = "My dad sent his steak back twice. When it finally came he clapped for it. The waiter said, 'Sir, that's not how well done works.'"


def output_dir() -> str:
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return value
    return "/output"


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"text must be 1..280 characters, got {len(TEXT)}"

    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
