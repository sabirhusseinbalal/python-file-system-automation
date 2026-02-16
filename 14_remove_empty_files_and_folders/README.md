# Remove Empty Files & Folders

## Description
Cleans up a folder by removing all empty files and empty folders. Works recursively, including all subfolders, and preserves non-empty files and folders.

**Note:** Only empty files and folders are removed; everything else remains intact.

## Modules Used
- `pathlib` – modern file system handling

## Features
- Recursive scanning of all files and folders
- Deletes empty files safely
- Deletes empty folders safely (bottom-up to avoid errors)
- Prints a summary of files checked and removed
- Beginner-friendly and readable code


## Project Structure
```
14_remove_empty_files_and_folders/
├── input/
│ └── ... # Add your files/folders here
├── main.py
└── README.md
```