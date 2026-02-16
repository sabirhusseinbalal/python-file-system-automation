# Search and Filter Files

## Description
Searches and filters files in a folder in multiple ways. You can filter by extension, name, size, or search inside file content. The tool works recursively and shows relative paths and file sizes.

## Modules Used
- `pathlib` – handle file paths

## Features
- Filter by extension, name, size, or content
- Handles subfolders automatically
- Skips files that cannot be read (binary files, permissions)
- Shows relative paths and file sizes
- Beginner-friendly and readable code

## Example Usage
### Folder structure:

```
input/
├── data/
│   ├── backup_data.txt
│   ├── data.csv
│   └── sales_data.csv
├── logs/
│   ├── error.log
│   └── system.log
├── reports/
│   ├── final_report.txt
│   └── summary.md
└── scripts/
    ├── helper.py
    ├── main.py
    └── test_script.py

```

### Filter by extension:

```
Enter extension (example: .py): .py

Total matched files: 3
File: scripts/helper.py - Size 150 bytes
File: scripts/main.py - Size 217 bytes
File: scripts/test_script.py - Size 130 bytes
```

### Search by file name:

```
Enter file name (example: main.py): main.py

Total matched files: 1
File: scripts/main.py - Size 217 bytes
```

### Filter by size (KB):

```
Enter max file size in KB: 150

Total matched files: 6
File: data/backup_data.txt - Size 94 bytes
File: data/data.csv - Size 52 bytes
File: data/sales_data.csv - Size 53 bytes
File: logs/error.log - Size 114 bytes
File: logs/system.log - Size 80 bytes
File: scripts/helper.py - Size 150 bytes
```

### Search inside file content:

```
Enter text to search inside files: Welcome

Total matched files: 2
File: reports/final_report.txt - Size 84 bytes
File: scripts/helper.py - Size 150 bytes
```


## Project Structure
```
18_search_and_filter_files/
├── input/
│ └── ... # Default Folder with files to search/filter
├── test/ 
├── main.py
└── README.md
```