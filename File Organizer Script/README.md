# File Organizer Script

A Python automation tool that scans a directory, categorizes files based on their extensions, and automatically organizes them into category-specific folders.

## Features

✅ **Automatic File Scanning** - Recursively scans a directory for files  
✅ **Smart Categorization** - Groups files by common types (images, documents, videos, audio, archives)  
✅ **Auto-Folder Creation** - Automatically creates category folders if they don't exist  
✅ **Duplicate Handling** - Handles file name conflicts by appending a counter  
✅ **Error Handling** - Gracefully handles missing directories and permission errors  
✅ **Progress Reporting** - Shows real-time feedback during organization  

## File Categories

| Category | Extensions |
|----------|-----------|
| **images** | .jpg, .jpeg, .png, .gif, .bmp, .svg, .ico, .webp |
| **documents** | .pdf, .doc, .docx, .txt, .xlsx, .xls, .ppt, .pptx, .odt |
| **videos** | .mp4, .avi, .mov, .mkv, .wmv, .flv, .webm, .m4v |
| **audio** | .mp3, .wav, .aac, .flac, .m4a, .wma, .ogg |
| **archives** | .zip, .rar, .7z, .tar, .gz, .bz2 |
| **others** | Any unmatched files |

## Required Modules

- `os` - Standard library for OS operations
- `shutil` - Standard library for file operations
- `pathlib` - Standard library for path handling

## How to Use

### Method 1: Interactive Mode
```bash
python main.py
```
Follow the prompt to enter the directory path you want to organize.

### Method 2: Programmatically
```python
from main import organize_files

# Organize a specific directory
stats = organize_files("C:/Users/YourUser/Downloads")
print(stats)  # {'total': 10, 'organized': 10, 'failed': 0}
```

### Using Individual Functions
```python
from main import scan_directory, categorize_file, move_file

# Scan a directory
files = scan_directory("./my_folder")

# Categorize a file
category = categorize_file("document.pdf")  # Returns 'documents'

# Move a single file
move_file("./my_folder/image.jpg", "./my_folder/images")
```

## Functions Overview

### `scan_directory(path)`
- **Purpose**: Lists all files in a directory
- **Input**: Directory path (string)
- **Output**: List of filenames (excluding subdirectories)

### `categorize_file(filename)`
- **Purpose**: Determines file category based on extension
- **Input**: Filename or filepath
- **Output**: Category name (string)

### `move_file(source, destination_folder)`
- **Purpose**: Moves a file to a destination folder
- **Input**: Source file path, destination folder path
- **Output**: Boolean (True if successful, False otherwise)
- **Side Effects**: Creates destination folder if needed

### `organize_files(directory)`
- **Purpose**: Main orchestration function that organizes all files
- **Input**: Directory path
- **Output**: Dictionary with statistics

### `main()`
- **Purpose**: Entry point with user interaction
- **Behavior**: Prompts for directory input and calls `organize_files()`

## Example Output

```
==================================================
Starting file organization in: C:/Downloads
==================================================

Found 12 file(s) to organize.

Created folder: C:/Downloads/images
Moved: photo.jpg → C:/Downloads/images
Moved: screenshot.png → C:/Downloads/images
Created folder: C:/Downloads/documents
Moved: resume.pdf → C:/Downloads/documents
Moved: notes.txt → C:/Downloads/documents
Created folder: C:/Downloads/videos
Moved: tutorial.mp4 → C:/Downloads/videos

==================================================
Organization Complete!
==================================================
Total files: 12
Organized: 12
Failed: 0
==================================================
```

## Learning Outcomes

This script demonstrates:
- **File System Operations** with `os` module
- **File Moving/Copying** with `shutil` module
- **Directory Traversal** and file enumeration
- **Loop Control** for processing collections
- **Conditional Logic** for categorization
- **Error Handling** with try-except blocks
- **String Manipulation** for file extensions
- **Function Design** and code organization

## Tips & Customization

### Add New File Categories
Edit the `FILE_CATEGORIES` dictionary:
```python
FILE_CATEGORIES = {
    'images': ['.jpg', '.png', '.gif'],
    'documents': ['.pdf', '.doc', '.xlsx'],
    'your_category': ['.ext1', '.ext2'],  # Add here
}
```

### Change Organization Behavior
Modify the `organize_files()` function to:
- Create nested category folders by date
- Skip certain file types
- Apply additional filtering logic

## Safety Features

- ✅ **No Destructive Operations** - Uses `shutil.move()` which is safe
- ✅ **Duplicate Prevention** - Detects and renames files that would conflict
- ✅ **Validation** - Checks directory existence before processing
- ✅ **Error Recovery** - Continues processing on single file failures

## Limitations

- Does not support moving directories themselves
- Only organizes the first level of files (not recursive subdirectories)
- Does not delete empty source directories after moving

## Future Enhancements

- [ ] Recursive directory organization
- [ ] Undo functionality
- [ ] Configuration file for custom categories
- [ ] Scheduled/automated organization
- [ ] Filtering by date or size

## License

Free to use and modify for educational purposes.
