# Compress Files & Folders

## Description
Compresses a file or an entire folder into a ZIP archive inside the output/ folder. The archive uses the original name of the file or folder, and existing output is handled safely.

for example:
- `notes.txt` → `notes.zip`
- `photos/` → `photos.zip`

## Modules Used
- `pathlib` – modern and safe file/folder path handling
- `shutil` – for creating ZIP archives

## Features
- Compresses both files and folders
- Handles existing output folder safely
- Uses clean archive names (no `.txt.zip`)
- Beginner-friendly and readable code


## Project Structure
```
09_compress_files_and_folders/
├── input/
│   └── ...           # File or folder to compress
├── output/           
│   └── ...           # ZIP file created here
├── test/             # Dummy data for testing
├── main.py
└── README.md
```