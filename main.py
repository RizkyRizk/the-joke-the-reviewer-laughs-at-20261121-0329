#!/usr/bin/env python3
"""Write one original one-line joke about working beside AI coding agents."""

import os

JOKE = "I asked my agent to fix one bug; it touched 47 files, and its only review comment was 'trust me'."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)

    # Verify what was actually written: read it back and check the gate.
    with open("/output/entry.txt", encoding="utf-8") as f:
        text = f.read()
    if not 1 <= len(text) <= 280 or not text.strip():
        raise SystemExit(
            "entry.txt failed verification: "
            f"{len(text)} characters, whitespace-only={not text.strip()}"
        )
    print(f"entry.txt OK: {len(text)} characters")


if __name__ == "__main__":
    main()
