from pathlib import Path
import shutil


BASE_DIR = Path(__file__).resolve().parent

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent

def remover(path):
    empty_files = 0
    empty_folders = 0

    # 1 Remove empty files
    files = [f for f in path.rglob("*") if f.is_file()]

    for file in sorted(files, key=lambda f: f.name.lower()):
        if file.stat().st_size == 0:
            file.unlink()  # delete file
            print(f"Removed empty file: {file.relative_to(BASE_DIR)}")
            empty_files += 1

    # 2 Remove empty folders (bottom-up)
    folders = [f for f in path.rglob("*") if f.is_dir()]
    
    for folder in sorted(folders, key=lambda f: len(f.parts), reverse=True):
        if not any(folder.iterdir()):  # folder is empty
            folder.rmdir()
            print(f"Removed empty folder: {folder.relative_to(BASE_DIR)}")
            empty_folders += 1

    total_files = len(files)
    print(f"\nTotal files checked: {total_files}")
    print(f"Empty files removed: {empty_files}")
    print(f"Empty folders removed: {empty_folders}")



       
while True:
    print()
    confirm = input("This will remove empty files only folder the 'input' folder. Continue? (y/n or 'q' to quit): ").lower()
    print()

    if confirm == 'q':
        print("Exiting...")
        break

    if confirm == 'n':
        print("Cancelled.")
        break

    if confirm == 'y':
        default_folder = BASE_DIR / "input"

        if default_folder.is_dir():
            print(f"Folder exists: {default_folder}")
            try:
                path = Path(default_folder)
                remover(path)
            except Exception as e:
                print(f"Error: {e}")
                continue
        else:
            print("Input folder is missing.")
            break
    else:
        print("Please choose a valid option (y/n/q).")
