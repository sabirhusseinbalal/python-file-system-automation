from pathlib import Path
import os
import sys


BASE_DIR = Path(__file__).resolve().parent


def permission_checker(path):


    total_items = 0
    readable_count = 0
    writable_count = 0
    executable_count = 0

    
    try:
        for file in path.rglob("*"):
            if file.is_file():

                # Item Count
                total_items+=1

                # Checking...
                readable = os.access(file, os.R_OK)
                writable = os.access(file, os.W_OK)
                executable = os.access(file, os.X_OK)
                    
                print("----")
                print(file.relative_to(path))

                # True - Yes | False - No

                if readable:
                    print(f"Readable: Yes")
                    readable_count+=1
                else:
                    print(f"Readable: No")

                if writable:
                    print(f"Writable: Yes")
                    writable_count+=1
                else:
                    print(f"Writable: No")

                if executable:
                    executable_count+=1
                    print(f"Executable: Yes")
                else:
                    print(f"Executable: No")

                print()
                print()
            
    except Exception as e:
        print(f"Error: {e}")

    # Result
    print(f"Total: {total_items}")  
    print(f"Readable: {readable_count}")  
    print(f"Writable: {writable_count}")  
    print(f"Executable: {executable_count}")  

    
    
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
            permission_checker(path)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Folder not found. Please enter a valid folder path.")
