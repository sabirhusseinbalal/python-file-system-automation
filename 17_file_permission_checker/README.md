# File Permission Checker

## Description
Checks file permissions inside a folder. It tells whether each file is readable, writable, and executable, scanning all files recursively.

It tells whether each file is:

- Readable
- Writable
- Executable

The program scans all files recursively inside the given folder.

## Modules Used
- `pathlib` – handle file paths
- `os` – check file permissions

## Features
- Recursive scanning of files
- Checks read, write, and execute permissions
- Copies empty folders
- Displays results in a clear format
- Shows summary count at the end
- Beginner-friendly logic


## Project Structure
```
17_file_permission_checker/
├── input/
│ └── ... # Default folder
├── test/ 
├── main.py
└── README.md
```