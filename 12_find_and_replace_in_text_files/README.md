# Find and Replace in Text Files

## Description
Edits text files in two ways: line-based editing (change a specific line) and word-based replacement (replace all occurrences of a word).

for example:
```
Some days you feel strong.
Some days you feel confused.
Both days are part of growth.
```
**Using word-based replace:**
```
Find: days
Replace with: nights
```
**Updated file becomes:**
```
Some nights you feel strong.
Some nights you feel confused.
Both nights are part of growth.
```
---

## Modules Used
- `pathlib` – modern file system handling

## Features
- Open a file using full path
- Use a default file if no path is provided
- Line-by-line editing
- Replace all occurrences of a word


## Project Structure
```
12_find_and_replace_in_text_files/
├── input/
│ └── ... # default file
├── main.py
└── README.md
```
