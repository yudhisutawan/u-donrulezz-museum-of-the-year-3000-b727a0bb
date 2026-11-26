"""Museum of the Year 3000 — winning museum label.

Writes exactly one line (103 characters) to the output entry file.
Stdlib only. The grader runs this with no network and no arguments;
the output directory is $MAKEFUN_OUTPUT_DIR, falling back to /output.
"""

import os

ENTRY = (
    "Ceiling oracle; it screamed at burnt toast, and citizens waved "
    "towels beneath it until it forgave them."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
