# File Organizer Script - Learning Guide

## Overview

This File Organizer Script is designed to teach you core Python concepts related to file system operations, data organization, and practical automation. It demonstrates professional coding practices while remaining beginner-friendly.

## Learning Objectives

By studying this script, you will learn:

1. **OS Operations** - How to interact with the file system
2. **File Management** - Moving, copying, and organizing files
3. **Loops & Iteration** - Processing collections of data
4. **Error Handling** - Managing exceptions gracefully
5. **Function Design** - Writing modular, reusable code
6. **Conditional Logic** - Making decisions based on data

---

## Key Concepts Explained

### 1. OS Operations (`os` module)

The `os` module provides functions to interact with the operating system.

#### Getting Directory Contents
```python
import os

files = os.listdir("./my_folder")  # Get all items in a directory
print(files)  # ['file1.txt', 'folder1', 'file2.jpg']
```

#### Checking File vs Directory
```python
# Check if something is a file
if os.path.isfile("path/to/item"):
    print("It's a file")

# Check if something is a directory
if os.path.isdir("path/to/item"):
    print("It's a folder")

# Check if path exists
if os.path.exists("path/to/item"):
    print("Path exists")
```

#### Getting File Information
```python
# Get file extension
filename = "document.pdf"
name, ext = os.path.splitext(filename)
print(ext)  # '.pdf'

# Get file path components
full_path = "/home/user/documents/file.txt"
directory = os.path.dirname(full_path)  # '/home/user/documents'
filename = os.path.basename(full_path)  # 'file.txt'
name, ext = os.path.splitext(filename)  # ('file', '.txt')

# Get absolute path
abs_path = os.path.abspath("./my_file.txt")

# Get current working directory
current = os.getcwd()

# Change current directory
os.chdir("/home/user/documents")
```

#### Creating Directories
```python
# Create a single directory (fails if parent doesn't exist)
os.mkdir("new_folder")

# Create directories recursively (creates parent directories as needed)
os.makedirs("path/to/nested/folders")
```

----

### 2. File Management (`shutil` module)

The `shutil` module provides higher-level file operations.

#### Moving Files
```python
import shutil

# Move a file (works across drives on Windows)
shutil.move("source/file.txt", "destination/file.txt")

# If destination is a directory, file is moved inside it
shutil.move("file.txt", "destination_folder/")
```

#### Copying Files
```python
# Copy a single file
shutil.copy("original.txt", "copy.txt")

# Copy with metadata (timestamps, permissions)
shutil.copy2("original.txt", "copy.txt")
```

#### Comparing with `os.rename()`
```python
# DIFFERENCE: os.rename() fails across drives on Windows
# shutil.move() works everywhere

# Use shutil.move() for reliability across different systems
```

---

### 3. Loops & Iteration

Processing multiple files requires looping through collections.

#### Basic Loop Through Files
```python
import os

directory = "./my_folder"

# Loop through all items
for item in os.listdir(directory):
    print(item)
    # Output: file1.txt, folder1, file2.jpg, ...

# Loop with full path
for item in os.listdir(directory):
    full_path = os.path.join(directory, item)
    if os.path.isfile(full_path):
        print(f"File: {item}")
```

#### Loop with Enumeration
```python
files = ["photo1.jpg", "photo2.jpg", "photo3.jpg"]

for index, filename in enumerate(files):
    print(f"{index}: {filename}")
    # Output:
    # 0: photo1.jpg
    # 1: photo2.jpg
    # 2: photo3.jpg
```

#### Nested Loops
```python
# Processing files in categories (nested loop)
FILE_CATEGORIES = {
    'images': ['.jpg', '.png'],
    'documents': ['.pdf', '.doc']
}

for category, extensions in FILE_CATEGORIES.items():
    print(f"{category}:")
    for ext in extensions:
        print(f"  {ext}")
```

---

### 4. Conditional Logic & Categorization

Making decisions based on file properties.

#### String Methods for Filtering
```python
filename = "document.pdf"

# Check if filename ends with extension
if filename.endswith('.pdf'):
    print("It's a PDF")

# Case-insensitive comparison
ext = filename.split('.')[-1].lower()
if ext in ['jpg', 'png', 'gif']:
    print("It's an image")
```

#### Dictionary Lookups for Categorization
```python
FILE_CATEGORIES = {
    'images': ['.jpg', '.jpeg', '.png'],
    'documents': ['.pdf', '.doc'],
}

def get_category(filename):
    ext = os.path.splitext(filename)[1].lower()
    
    # Loop through categories
    for category, extensions in FILE_CATEGORIES.items():
        if ext in extensions:
            return category
    
    return 'others'  # Default category

print(get_category("photo.jpg"))      # 'images'
print(get_category("resume.pdf"))     # 'documents'
print(get_category("script.py"))      # 'others'
```

---

### 5. Error Handling

Managing exceptions when files don't exist or permissions are denied.

#### Try-Except Blocks
```python
import os

# WITHOUT error handling (crashes):
files = os.listdir("/nonexistent/folder")

# WITH error handling (graceful):
try:
    files = os.listdir("/nonexistent/folder")
except FileNotFoundError:
    print("Folder doesn't exist")
    files = []
except PermissionError:
    print("Access denied")
    files = []
```

#### Common File Exceptions
```python
try:
    # File operations
    f = open("file.txt", "r")
except FileNotFoundError:
    print("File not found")
except IsADirectoryError:
    print("That's a directory, not a file")
except PermissionError:
    print("Permission denied")
except Exception as e:
    print(f"Unexpected error: {e}")
```

---

### 6. Function Design & Modularity

Breaking code into reusable functions.

#### Single Responsibility
Each function should do ONE thing:

```python
# ✓ GOOD: Each function has one job
def scan_directory(path):
    """Lists files in directory"""
    return os.listdir(path)

def categorize_file(filename):
    """Determines file category"""
    return ...

def move_file(source, dest):
    """Moves a file"""
    return shutil.move(source, dest)

# ✗ BAD: Does too much
def do_everything(path):
    files = os.listdir(path)
    for file in files:
        category = ...
        shutil.move(...)
    # Hard to test or reuse
```

#### Composable Functions
```python
# You can combine simple functions to build complex workflows

# Simple functions
files = scan_directory(directory)
category = categorize_file(file)
move_file(source, dest)

# Composed into a workflow
for file in scan_directory(directory):
    category = categorize_file(file)
    dest_folder = os.path.join(directory, category)
    move_file(file, dest_folder)
```

---

## Step-by-Step Code Walkthrough

### Function 1: `scan_directory(path)`

```python
def scan_directory(path):
    """Scan a directory and return a list of files."""
    try:
        files = []
        # LOOP through all items in the directory
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            # CONDITIONAL: only include files, not directories
            if os.path.isfile(item_path):
                files.append(item)
        return files
    except FileNotFoundError:
        print(f"Error: Directory '{path}' not found.")
        return []
```

**Key Concepts:**
- Try-except for error handling
- Loop with `os.listdir()`
- Conditional check with `os.path.isfile()`
- Building a result list

---

### Function 2: `categorize_file(filename)`

```python
def categorize_file(filename):
    """Categorize a file based on its extension."""
    # Get file extension using os.path.splitext()
    file_extension = os.path.splitext(filename)[1].lower()
    
    # LOOP through categories to find a match
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension in extensions:
            return category
    
    return 'others'  # Default if no match
```

**Key Concepts:**
- String methods: `.lower()`, `.splitext()`
- Dictionary iteration: `.items()`
- Membership testing: `in` operator
- Default return value

---

### Function 3: `move_file(source, destination_folder)`

```python
def move_file(source, destination_folder):
    """Move a file to a destination folder."""
    try:
        # Create destination if it doesn't exist
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        
        # Build the destination path
        filename = os.path.basename(source)
        destination_path = os.path.join(destination_folder, filename)
        
        # Handle duplicates
        if os.path.exists(destination_path):
            name, ext = os.path.splitext(filename)
            counter = 1
            # LOOP to find an available filename
            while os.path.exists(destination_path):
                new_filename = f"{name}_{counter}{ext}"
                destination_path = os.path.join(destination_folder, new_filename)
                counter += 1
        
        # Move the file using shutil
        shutil.move(source, destination_path)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
```

**Key Concepts:**
- Conditional folder creation
- Path joining with `os.path.join()`
- While loop for finding unique names
- Error handling with broad exception catch

---

### Function 4: `organize_files(directory)`

```python
def organize_files(directory):
    """Main orchestration function."""
    # Step 1: List all files
    files = scan_directory(directory)
    
    if not files:
        return {'total': 0, 'organized': 0, 'failed': 0}
    
    stats = {'total': len(files), 'organized': 0, 'failed': 0}
    
    # Step 2: LOOP through files and organize
    for file in files:
        source_path = os.path.join(directory, file)
        
        if os.path.isdir(source_path):
            continue  # Skip directories
        
        # Step 3: Categorize each file
        category = categorize_file(file)
        destination_folder = os.path.join(directory, category)
        
        # Step 4: Move the file
        if move_file(source_path, destination_folder):
            stats['organized'] += 1
        else:
            stats['failed'] += 1
    
    return stats
```

**Key Concepts:**
- Composition of smaller functions
- Loop with statistics tracking
- Conditional skip with `continue`
- Dictionary for returning multiple values

---

## Common Patterns

### Pattern 1: Safe File Listing
```python
files = []
try:
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            files.append(item)
except (FileNotFoundError, PermissionError) as e:
    print(f"Error: {e}")
```

### Pattern 2: File Extension Detection
```python
ext = os.path.splitext(filename)[1].lower()
if ext in ['.jpg', '.png', '.gif']:
    print("Image file")
```

### Pattern 3: Safe File Moving
```python
if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)

dest_path = os.path.join(dest_folder, os.path.basename(source))
shutil.move(source, dest_path)
```

### Pattern 4: Building Paths
```python
# Always use os.path.join() for cross-platform compatibility
path = os.path.join(directory, "subfolder", "file.txt")
# Windows: directory\subfolder\file.txt
# Linux/Mac: directory/subfolder/file.txt
```

---

## Exercises

Try modifying the script to:

1. **Filter by Size**: Only organize files larger than 1MB
   ```python
   size = os.path.getsize(file_path)
   if size > 1_000_000:
       # organize...
   ```

2. **Filter by Date**: Only organize files modified in the last 7 days
   ```python
   import time
   modified = os.path.getmtime(file_path)
   if time.time() - modified < 7 * 24 * 3600:
       # organize...
   ```

3. **Organize by Date**: Create folders by year/month instead of type
   ```python
   import datetime
   created = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
   folder = created.strftime("Year_%Y/Month_%m")
   ```

4. **Recursive Organization**: Organize files in all subdirectories
   ```python
   for root, dirs, files in os.walk(directory):
       # root: current directory
       # dirs: subdirectories
       # files: files in current directory
   ```

5. **Undo Functionality**: Move files back to original location
   ```python
   # Track original locations before moving
   # Create a JSON file with: {moved_file: original_path}
   # Load and restore from JSON on undo command
   ```

---

## Key Takeaways

✅ Use `os` module for file system operations  
✅ Use `shutil` for moving/copying files  
✅ Always use `os.path.join()` for path compatibility  
✅ Loop through collections with `for` loops  
✅ Use `try-except` for error handling  
✅ Break code into small, focused functions  
✅ Make decisions with conditionals (`if/elif/else`)  
✅ Test with different file types and directories  

---

## Resources

- [Python `os` module documentation](https://docs.python.org/3/library/os.html)
- [Python `shutil` module documentation](https://docs.python.org/3/library/shutil.html)
- [Python exception handling](https://docs.python.org/3/tutorial/errors.html)
- [f-strings formatting](https://docs.python.org/3/tutorial/inputandoutput.html#tidy-output-formatting)

