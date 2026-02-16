from pathlib import Path
import shutil
import zipfile

BASE_DIR = Path(__file__).resolve().parent

# Extract a ZIP file into the output folder
def extract(path):

    output_dir = BASE_DIR / "output"

    if output_dir.exists():
        confirm = input("Output folder exists. Delete and continue? (y/n): ").lower()
        if confirm != "y":
            print("Cancelled.")
            return
        shutil.rmtree(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        extract_folder = output_dir / path.stem

        with zipfile.ZipFile(path, 'r') as zip_ref:
            # Open ZIP file and extract all contents
            zip_ref.extractall(extract_folder)
            print(f"Extracted '{path}' to '{extract_folder}' successfully.")

    except Exception as e:
        print(f"Error while extracting: {e}")
   


while True:
    print()
    user_path = input("Enter full path of file (or 'q' to quit): ").strip()
    print()

    default_file = BASE_DIR / "input" / "data.zip"

    if user_path.lower() == 'q':
        print("Exiting...")
        break

    if not user_path:
        path = default_file
        if path.is_file():
            # Uses default file if no path provided
            print(f"No path provided — using default file: {path}")
        else:
            print("Default file is missing.")
            continue
    else:
        path = Path(user_path)
    
    if path.is_file() and path.suffix==".zip":
        try:
            print(f"ZIP file exists: {path}")
            extract(path)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("404 - Please enter a valid zip file path.")

