"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one roast of a daily gadget: the smart speaker that
# answers questions nobody asked and ignores the ones shouted at it.
# One sentence, 127 characters — inside the 200-character gate.
# Revision note: the relationship comparison is the sting, so it stays last.
import os

TEXT = (
    "My smart speaker answers questions I never asked and ignores "
    "the ones I shout, which is exactly how my last relationship ended."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
