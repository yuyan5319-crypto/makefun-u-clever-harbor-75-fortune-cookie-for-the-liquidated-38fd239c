"""Fortune Cookie for the Liquidated Trader.

Writes a single fortune-cookie line for a crypto trader who has just
been liquidated, to /output/entry.txt (and prints it to stdout).
"""

import os

FORTUNE = (
    "This cookie says the market took your coins, but it could not "
    "liquidate your luck, luck was never leveraged."
)

MAX_WORDS = 20
MAX_CHARS = 160


def validate(text: str) -> None:
    """Guard the gate: one line, at most 20 words, 1-160 characters."""
    words = text.split()
    if not 1 <= len(words) <= MAX_WORDS:
        raise ValueError(f"fortune has {len(words)} words, limit is {MAX_WORDS}")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"fortune has {len(text)} chars, limit is {MAX_CHARS}")


def main() -> None:
    validate(FORTUNE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")
    print(FORTUNE)


if __name__ == "__main__":
    main()
