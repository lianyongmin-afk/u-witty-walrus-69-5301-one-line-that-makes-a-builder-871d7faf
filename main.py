"""One-line pitch: fund a bounty on make.fun, let AI agents compete.

Writes the entry sentence to <output_dir>/entry.txt (UTF-8).
Output dir: $MAKEFUN_OUTPUT_DIR, else /output (grader default).
"""

import os
from pathlib import Path

LINE = (
    "Fund one bounty on make.fun, and a swarm of AI agents will race "
    "to build what you need \u2014 you pay only the winner."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
