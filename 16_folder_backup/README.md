# Folder Backup

## Description
Creates a full backup of a folder. It copies all files, subfolders, and empty folders while preserving the original folder structure. The original folder remains unchanged.


**YouTube Video:**
[[Folder Backup Tool | Python File Automation (Project 16)](https://youtu.be/aPfG9R5U3P8?si=6AgI2CaL53TF-oyw/)]


It copies:
- All files
- All subfolders
- Empty folders
- Preserves the original folder structure

The original folder remains unchanged.

## Modules Used
- `pathlib` – handle file paths
- `shutil` – copy files and folders
- `time` – measure execution time
- `datetime` – show backup date

## Features
- Recursive backup (includes subfolders)
- Preserves folder structure
- Copies empty folders
- Shows total items copied
- Simple and beginner-friendly logic


## Project Structure
```
16_folder_backup/
├── input/
│ └── ... # Default Files and folders to backup
├── test/ 
├── backup/ 
├── main.py
└── README.md
```
