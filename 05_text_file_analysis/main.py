from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def analyze_file(file):
    # Read all lines from file
    lines = file.readlines()

    # Combine lines into single text
    text = "".join(lines)

    # Calculate basic statistics
    chars = len(text)
    words = len(text.split())

    print(f"Lines: {len(lines)}, Words: {words}, Chars: {chars}")


while True:
    print()
    user_path = input("Enter full file path (or 'q' to quit): ").strip()
    print()

    default_file = BASE_DIR / "input" / "story.txt"

    if user_path.lower() == 'q':
        print("Exiting...")
        break

    if not user_path:
        path = default_file
        if path.is_file():
            print(f"No path provided — using default file: {default_file.name}")
        else:
            print("No path provided and default file is missing.")
            continue
    else:
        path = Path(user_path)

    if path.is_file() and path.suffix == ".txt":
        try:
            with path.open("r", encoding="utf-8") as file:
                print(f"File loaded successfully: {path.name}")
                analyze_file(file)
        except Exception:
            print("Failed to open file.")
    else:
        print("Invalid file or file not found.")
