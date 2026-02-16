from pathlib import Path
import shutil

BASE_DIR = Path(__file__).resolve().parent

def split(path):
    output_dir = BASE_DIR / "output"
    
    # Handle existing output folder
    if output_dir.exists():
        confirm = input("Output folder exists. Delete and continue? (y/n): ").lower()
        if confirm != "y":
            print("Cancelled.")
            return
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    data = []

    for file in path.rglob("*"):
        if file.is_file():
            data.append(file)



    folder_count = 1
    start = 0
    total = len(data)
    x = 9 # files per folder


    try:
        while start < total:
            files = data[start:start+x]
            if not files:
                break  # stop if no files

            folder_path = output_dir / f"folder{folder_count}"
            folder_path.mkdir(parents=True, exist_ok=True)

            for file in files:
                # handle duplicate names
                dest_file = folder_path / file.name
                suffix = 1
                while dest_file.exists():
                    dest_file = folder_path / f"{file.stem}_{suffix}{file.suffix}"
                    suffix += 1

                shutil.move(str(file), dest_file)
                print(f"File: {file.name} → moved to {folder_path}")

            folder_count += 1
            start += x

    except Exception as e:
        print(f"Error: {e}")

    print(f"{total} files split into {folder_count-1} subfolders successfully.")


       

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
            split(path)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Folder not found. Please enter a valid folder path.")
