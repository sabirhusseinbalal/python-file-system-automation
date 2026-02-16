# Folder Size Analyzer

## Description
Analyzes the total size and number of files in a folder, including all nested files and subfolders, and prints a human-readable size (Bytes, KB, MB, etc.).

for example:
```
Enter full folder path (or 'q' to quit): input
Folder exists: input
Folder: input
Total Files: 32
Total Size: 1.43 KB
```
---

## Modules Used
- `pathlib` – modern path handling

## Features
- Counts all files inside a folder.
- Calculates total size in Bytes, KB, MB, etc.
- Handles empty folders and very small files properly.


## Project Structure
```
13_folder_size_analyzer/
├── input/
│   └── ...           # files
├── main.py
└── README.md
```

***Notes:*** **only files are counted, folder sizes themselves not included**