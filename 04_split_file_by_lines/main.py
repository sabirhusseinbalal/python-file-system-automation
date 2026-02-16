from pathlib import Path
import shutil

BASE_DIR = Path(__file__).resolve().parent


def split_file(file):
    # Remove old output folder so results stay clean
    output_dir = BASE_DIR / "output"
    if output_dir.exists():
        shutil.rmtree(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    # how many lines per file
    while True:
        try:
            x = input("Enter number of lines per file (or press 'q' to go back): ")

            if x.lower() == "q":
                print("Going back to file selection...")
                return

            x = int(x)
            if x > 0:
                break

            raise ValueError()

        except ValueError:
            print("Please enter a valid number.")

    file_count = 1
    start = 0

    # Read all lines from file
    lines = file.readlines()
    total_lines = len(lines)

    try:
        # Create new file for each chunk of lines
        while start < total_lines:
            file_path = output_dir / f"file{file_count}.txt"
            data = lines[start:start + x]

            with open(file_path, "w", encoding="utf-8") as out:
                for line in data:
                    out.write(line)

            print(f"Part {file_count} created successfully → {file_path}")

            file_count += 1
            start += x

    except Exception as e:
        print(f"Error: {e}")

    print("New data replaced the old output successfully...")


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
                split_file(file)
        except Exception:
            print("Failed to open file.")
    else:
        print("Invalid file or file not found.")
