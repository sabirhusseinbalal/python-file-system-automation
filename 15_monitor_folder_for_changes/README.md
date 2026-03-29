# Folder Monitor

## Description
Monitors a folder and shows file changes in real time. It detects created, deleted, modified, and moved files. The program runs continuously until stopped manually.


**YouTube Video:**
[[Folder Monitor | Python File Automation (Project 15)](https://youtu.be/6jGcJnxQyLw?si=Sb7uFqlXzjdcrHkD/)]


It detects:
- Created files
- Deleted files
- Modified files
- Moved files

The program runs continuously until stopped manually.

## Modules Used
- `watchdog` – monitor file system events
- `pathlib` – handle folder paths
- `time` – keep program running

## Features
- Real-time folder monitoring
- Recursive scanning (includes subfolders)
- Simple OOP structure
- Clean and readable code


## Project Structure
```
15_monitor_folder_for_changes/
├── input/
│ └── ... #  Files to monitor
├── main.py
└── README.md
```
