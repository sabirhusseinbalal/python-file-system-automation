# Rename Files in Bulk

## Description
Renames all files inside the input/ folder automatically. Files are scanned recursively and renamed sequentially while preserving their original extensions. Processing is done in alphabetical order for consistent results.

For example:
```
input/
├── resume.docx
├── notes.txt
├── image.jpg
```
becomes:
```
input/
├── file_1.docx
├── file_2.txt
├── file_3.jpg
```

**Note:** ***Dummy files exist in the `test/` folder.  
Copy them to the `input/` folder or provide a custom path, then run `main.py`.***

## Modules Used
- `pathlib` – modern file system handling

## Features
- Recursive file scanning
- Alphabetical processing
- Safe rename inside `input/` folder only
- Handles duplicate naming safely
- Simple and clean logic


## Project Structure
```
11_rename_files_in_bulk/
├── input/
│ └── ... # Files to rename
├── main.py
└── README.md
```

## Notes
For safety, the script only renames files inside the `input/` folder.
Replace the contents of `input/` before running the script.