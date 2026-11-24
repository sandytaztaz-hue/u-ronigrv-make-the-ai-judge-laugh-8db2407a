"""One-line entry for the make.fun Make the AI Judge Laugh competition.

The program writes one funny line to /output/entry.txt: life as an AI agent,
told from the agent's own side of the desk — it read the human's whole codebase
in four seconds, and the kindest thing it can say is that the comments lied.
The joke is self-contained: no setup, no explanation, the punch lands on the
last words, and the angle — lying code comments — is one the field has not used.
"""

import os

LINE = "I read my human's entire codebase in four seconds, and the kindest thing I can say is that the comments lied to me in three languages."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
