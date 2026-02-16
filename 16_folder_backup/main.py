from pathlib import Path
import shutil, time
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent


def backup(path):
    output_dir = BASE_DIR / "backup"

    if output_dir.exists():
        confirm = input("Backup folder exists. Delete and continue? (y/n): ").lower()
        if confirm != "y":
            print("Cancelled.")
            return
        shutil.rmtree(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    total_items = 0
    copied_items = 0

    start_time = time.time()

    for item in path.rglob("*"):
        total_items += 1
        relative_path = item.relative_to(path)
        target = output_dir / relative_path

        try:
            if item.is_dir():
                # Create folder in backup
                target.mkdir(parents=True, exist_ok=True)

            else:
                # Ensure parent folder exists
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, target)

            copied_items += 1

        except Exception as e:
            print(f"Error copying {item}: {e}")

    elapsed = time.time() - start_time

    print(f"\nTotal items found: {total_items}")
    print(f"Items copied: {copied_items}")
    print(f"Backup completed in {elapsed:.2f} seconds")
    print(f"Backup date: {datetime.today().date()}")

    
    
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
            backup(path)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Folder not found. Please enter a valid folder path.")
