"""Dad Joke Showdown entry: one dad joke, written to /output/entry.txt.

The joke is a plain, straight-faced setup with a double mirror pun for the
punchline: "reflected on it" (thinking it over / a mirror reflecting) and
"cracked up" (bursting out laughing / a mirror cracking).
"""

import os

JOKE = "I told the mirror a joke, and it just reflected on it for a while, then cracked up."


def main() -> None:
    # Gate: the entry must be 1-200 characters of real text.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
