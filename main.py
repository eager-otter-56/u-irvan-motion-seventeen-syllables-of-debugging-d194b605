"""Entry for 'Seventeen Syllables of Debugging': a 5-7-5 haiku.

Cursor at 3am, a stack trace that stops at line nine, and the turn:
all of it was one misplaced comma.
"""
import os

ENTRY_TEXT = (
    "Cursor blinks at three\n"
    "the stack trace stops at line nine\n"
    "bug was a comma"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
