import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# Merge all CSV files inside a given folder
def merge_csv(path):
    output_dir = BASE_DIR / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        data = None
        col = []

        for item in sorted(path.iterdir()):
            if item.suffix != ".csv":
                print(f"Skipping '{item.name}': Invalid file type (only .csv allowed)")
                continue

            csv = pd.read_csv(item)
            col_names = list(csv.columns)

            if not col:
                # Use the first valid CSV as base schema
                col = col_names
                data = csv
                print(f"Loaded '{item.name}' as base CSV with columns: {col_names}")
            else:

                # Only files with matching column names are merged
                if set(col_names) == set(col):
                    csv = csv[col]
                    data = pd.concat([data, csv], axis=0)
                    print(f"Appended '{item.name}' ({len(csv)} rows)")
                else:
                    print(f"Skipped '{item.name}': column names don't match the base CSV ({col_names})")

        if data is not None:
            
            data = data.reset_index(drop=True)

            # Save final merged CSV into output folder
            file_path = output_dir / "data.csv"
            data.to_csv(file_path, index=False)
            print(f"\nMerged CSV saved to: {file_path} ({len(data)} total rows)")
        else:
            print("No valid CSV files found to merge.")

    except Exception as e:
        print(f"Error during merge: {e}")



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
            merge_csv(path)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Folder not found. Please enter a valid folder path.")
