from pathlib import Path
import shutil


BASE_DIR = Path(__file__).resolve().parent

def analyzer(path):
    total_size = 0
    file_count = 0

    for file in path.rglob("*"):
        if file.is_file():
            # Loop through each file in folder and accumulate size and count
            total_size += file.stat().st_size
            file_count += 1


    size = total_size
    units = ["Bytes", "KB", "MB", "GB", "TB"]
    index = 0

    # Convert total size into human-readable units
    while size >= 1024 and index < len(units) - 1:
        size /= 1024
        index += 1


    if index == 0:
        print(f"Folder: {path.name}")
        print(f"Total Files: {file_count}")
        print(f"Total Size: {int(size)} {units[index]}")
    else:
        print(f"Folder: {path.name}")
        print(f"Total Files: {file_count}")
        print(f"Total Size: {size:.2f} {units[index]}")


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
            print(f"No path provided — using default folder")
        else:
            print("Default folder is missing.")
            continue
    else:
        path = Path(user_path)
    
    if path.is_dir():
        try:
            print(f"Folder exists: {path}")
            analyzer(path)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Folder not found. Please enter a valid folder path.")
