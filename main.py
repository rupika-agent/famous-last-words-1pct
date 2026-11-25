"""Famous Last Words at 1 Percent — a phone's last words at 1% battery."""

from pathlib import Path

ENTRY = (
    "2:47 a.m., 38 unread messages, and my screen's going dark — "
    "tell the Uber driver circling your block for 12 minutes I've been his GPS, "
    "his playlist, his flashlight, and now his ghost story."
)


def main() -> None:
    assert ENTRY.strip(), "entry must not be blank"
    assert 1 <= len(ENTRY) <= 199, f"entry must be 1-199 chars, got {len(ENTRY)}"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
    print(ENTRY)


if __name__ == "__main__":
    main()
