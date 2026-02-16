import hashlib
from pathlib import Path
import shutil

BASE_DIR = Path(__file__).resolve().parent

def remove_duplicates(path):
    output_dir = BASE_DIR / "output"
    
    # Handle existing output folder
    if output_dir.exists():
        confirm = input("Output folder exists. Delete and continue? (y/n): ").lower()
        if confirm != "y":
            print("Cancelled.")
            return
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    seen_hashes = {}  # store hash: file name

    for file in sorted(path.iterdir()):
        if not file.is_file():
            continue

        # Compute file hash
        with file.open("rb") as f:
            file_hash = hashlib.md5(f.read()).hexdigest()

        if file_hash in seen_hashes:
            # Duplicate > move to output folder
            shutil.move(str(file), output_dir / file.name)
            print(f"Duplicate: {file.name} → moved to output/")
        else:
            # First occurrence > keep in input folder
            seen_hashes[file_hash] = file.name

    print(f"\nDone! {len(seen_hashes)} unique file(s) kept in input/, duplicates moved to output/")


            

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
            remove_duplicates(path)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Folder not found. Please enter a valid folder path.")
