from pathlib import Path

LINE = "I gave an agent our duplicate-file cleaner to tidy the shared drive, so it listened to standup and replaced my boss with a symlink to me."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(f"{LINE}\n", encoding="utf-8")


if __name__ == "__main__":
    main()
