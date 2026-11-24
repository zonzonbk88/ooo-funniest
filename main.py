"""The Funniest Out-of-Office — make.fun entry.

Writes a single funny out-of-office auto-reply line to entry.txt.
The reply must be exactly one line of 1-140 characters, no link.
"""

import os

LINE = (
    "I'm out of office until Monday. My auto-reply is out of office too, "
    "so this message was written by my cat, who has since resigned."
)


def main() -> None:
    # Enforce the competition gate before writing anything:
    # exactly one line, 1-140 characters, no link.
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 140, f"entry is {len(line)} chars, must be 1-140"
    assert "http" not in line and "www." not in line, "entry must contain no link"

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"Wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
