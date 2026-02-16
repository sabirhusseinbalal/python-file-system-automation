from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# 1 Filter by extension
def option_fileext(path):
    while True:
        try:
            user_input = input("Enter extension (example: .py) (or press 'q' to go back): ").strip()
            if user_input.lower() == 'q':
                print("Going back...\n")
                break

            if not user_input:
                print("Default .py extension set")
                user_input = ".py"

            matched_files = {}
            for file in path.rglob("*"):
                if file.is_file() and file.suffix == user_input:
                    matched_files[file.relative_to(path)] = file.stat().st_size

            print(f"Total matched files: {len(matched_files)}")
            for file, size in matched_files.items():
                print(f"File: {file} - Size: {size} bytes")
            print()

        except Exception as e:
            print(f"Error: {e}\n")

# 2 Search by filename
def option_filename(path):
    while True:
        try:
            user_input = input("Enter file name (example: main.py) (or press 'q' to go back): ").strip()
            if user_input.lower() == 'q':
                print("Going back...\n")
                break

            if not user_input:
                print("Default main.py name set")
                user_input = "main.py"

            matched_files = {}
            for file in path.rglob("*"):
                if file.is_file() and file.name == user_input:
                    matched_files[file.relative_to(path)] = file.stat().st_size

            print(f"Total matched files: {len(matched_files)}")
            for file, size in matched_files.items():
                print(f"File: {file} - Size: {size} bytes")
            print()

        except Exception as e:
            print(f"Error: {e}\n")

# 3 Filter by file size (KB)
def option_filesize(path):
    while True:
        try:
            user_input = input("Enter max file size in KB (example: 150) (or press 'q' to go back): ").strip()
            if user_input.lower() == 'q':
                print("Going back...\n")
                break

            if not user_input:
                print("Default 300 KB set")
                max_size = 300 * 1024
            else:
                max_size = int(user_input) * 1024

            matched_files = {}
            for file in path.rglob("*"):
                if file.is_file() and file.stat().st_size <= max_size:
                    matched_files[file.relative_to(path)] = file.stat().st_size

            print(f"Total matched files: {len(matched_files)}")
            for file, size in matched_files.items():
                print(f"File: {file} - Size: {size} bytes")
            print()

        except Exception as e:
            print(f"Error: {e}\n")

# 4 Search inside file content
def option_filecontent(path):
    while True:
        try:
            user_input = input("Enter text to search inside files (or press 'q' to go back): ").strip()
            if user_input.lower() == 'q':
                print("Going back...\n")
                break

            if not user_input:
                print("Default search text set: 'Welcome to the system'")
                user_input = "Welcome to the system"

            matched_files = {}
            for file in path.rglob("*"):
                if file.is_file():
                    try:
                        with file.open("r", encoding="utf-8") as f:
                            content = f.read()
                            if user_input in content:
                                matched_files[file.relative_to(path)] = file.stat().st_size
                    except:
                        # Ignore files that can't be read (binary, permission)
                        continue

            print(f"Total matched files: {len(matched_files)}")
            for file, size in matched_files.items():
                print(f"File: {file} - Size: {size} bytes")
            print()

        except Exception as e:
            print(f"Error: {e}\n")


# Main menu
def search_and_filter(path):
    while True:
        try:
            choice = input(
                "Choose filter type:\n"
                "1 - Filter by extension\n"
                "2 - Search by file name\n"
                "3 - Filter by max size (KB)\n"
                "4 - Search inside file content\n"
                ": (or press 'q' to go back): "
            ).strip()

            if choice.lower() == 'q':
                print("Going back...\n")
                break

            choice = int(choice)
            if choice == 1:
                option_fileext(path)
            elif choice == 2:
                option_filename(path)
            elif choice == 3:
                option_filesize(path)
            elif choice == 4:
                option_filecontent(path)
            else:
                print("Invalid choice.\n")

        except Exception as e:
            print(f"Error: {e}\n")


# Program start
while True:
    print()
    user_path = input("Enter full folder path (or 'q' to quit): ").strip()
    print()

    default_folder = BASE_DIR / "input"

    if user_path.lower() == 'q':
        print("Exiting...")
        break

    if not user_path:
        path = default_folder
        if path.is_dir():
            print(f"No path provided — using default folder: {path}")
        else:
            print("Default folder is missing.")
            continue
    else:
        path = Path(user_path)

    if path.is_dir():
        try:
            print(f"Folder exists: {path}")
            search_and_filter(path)
        except Exception as e:
            print(f"Error: {e}\n")
    else:
        print("Folder not found. Please enter a valid folder path.")
