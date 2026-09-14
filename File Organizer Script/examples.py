"""
Example usage of the File Organizer Script
Demonstrates all the main functions and how to use them.
"""

from main import (
    scan_directory,
    categorize_file,
    move_file,
    organize_files,
    FILE_CATEGORIES
)
import os


def example_1_scan_directory():
    """Example 1: Scanning a directory for files"""
    print("\n" + "="*50)
    print("EXAMPLE 1: Scanning a Directory")
    print("="*50)
    
    # Example: Scan current directory
    current_dir = os.getcwd()
    files = scan_directory(current_dir)
    
    print(f"\nDirectory: {current_dir}")
    print(f"Files found: {len(files)}\n")
    
    if files:
        for file in files[:5]:  # Show first 5 files
            print(f"  - {file}")
        if len(files) > 5:
            print(f"  ... and {len(files) - 5} more")
    else:
        print("  No files found")


def example_2_categorize_files():
    """Example 2: Categorizing files by extension"""
    print("\n" + "="*50)
    print("EXAMPLE 2: Categorizing Files")
    print("="*50)
    
    test_files = [
        "photo.jpg",
        "document.pdf",
        "video.mp4",
        "song.mp3",
        "archive.zip",
        "script.py",
        "notes.txt",
        "presentation.pptx"
    ]
    
    print("\nFile Categorization Results:\n")
    for filename in test_files:
        category = categorize_file(filename)
        print(f"  {filename:<20} → {category}")


def example_3_view_categories():
    """Example 3: View all available categories"""
    print("\n" + "="*50)
    print("EXAMPLE 3: Available File Categories")
    print("="*50)
    
    print("\nCategory Mappings:\n")
    for category, extensions in FILE_CATEGORIES.items():
        print(f"  {category.upper()}:")
        # Print extensions in rows of 4
        for i in range(0, len(extensions), 4):
            ext_list = extensions[i:i+4]
            print(f"    {', '.join(ext_list)}")
        print()


def example_4_demonstrate_logic():
    """Example 4: Step-by-step demonstration of organization logic"""
    print("\n" + "="*50)
    print("EXAMPLE 4: Organization Logic Flow")
    print("="*50)
    
    demo_dir = "demo_files"
    demo_files = [
        ("image1.jpg", "images"),
        ("document1.pdf", "documents"),
        ("video1.mp4", "videos"),
        ("song.mp3", "audio"),
        ("archive.zip", "archives"),
        ("readme.txt", "documents"),
    ]
    
    print(f"\nSimulating organization of '{demo_dir}' directory:\n")
    
    for filename, expected_category in demo_files:
        category = categorize_file(filename)
        status = "✓" if category == expected_category else "✗"
        destination = os.path.join(demo_dir, category)
        
        print(f"{status} File: {filename}")
        print(f"  → Category: {category}")
        print(f"  → Destination: {destination}")
        print()


def example_5_how_to_use_main_function():
    """Example 5: How to use the main organize_files function"""
    print("\n" + "="*50)
    print("EXAMPLE 5: Using organize_files() Function")
    print("="*50)
    
    print("\nUsage:\n")
    
    code_example = '''
# Basic usage:
from main import organize_files

# Organize a directory
stats = organize_files("C:/Users/YourUser/Downloads")

# Access statistics
print(f"Total files: {stats['total']}")
print(f"Organized: {stats['organized']}")
print(f"Failed: {stats['failed']}")

# The function will:
# 1. Scan the directory for all files
# 2. Categorize each file by extension
# 3. Create category folders if needed
# 4. Move files to their appropriate folders
# 5. Return a statistics dictionary
'''
    
    print(code_example)


def example_6_custom_implementation():
    """Example 6: Creating a custom implementation"""
    print("\n" + "="*50)
    print("EXAMPLE 6: Custom Implementation")
    print("="*50)
    
    example = '''
# You can create custom functions using the building blocks:

def organize_by_date(directory):
    """Organize files by creation date instead of type"""
    
    files = scan_directory(directory)
    
    for file in files:
        file_path = os.path.join(directory, file)
        # Get file creation date
        created = os.path.getctime(file_path)
        date_str = datetime.fromtimestamp(created).strftime("%Y-%m-%d")
        
        # Move to date folder
        date_folder = os.path.join(directory, date_str)
        move_file(file_path, date_folder)

def organize_by_size(directory):
    """Organize files by size categories"""
    
    files = scan_directory(directory)
    
    for file in files:
        file_path = os.path.join(directory, file)
        size = os.path.getsize(file_path)
        
        if size < 1_000_000:  # < 1 MB
            category = "small"
        elif size < 100_000_000:  # < 100 MB
            category = "medium"
        else:
            category = "large"
        
        folder = os.path.join(directory, category)
        move_file(file_path, folder)
'''
    
    print(example)


def main():
    """Run all examples"""
    print("\n" + "="*60)
    print(" "*10 + "FILE ORGANIZER SCRIPT - USAGE EXAMPLES")
    print("="*60)
    
    # Run all examples
    example_1_scan_directory()
    example_2_categorize_files()
    example_3_view_categories()
    example_4_demonstrate_logic()
    example_5_how_to_use_main_function()
    example_6_custom_implementation()
    
    print("\n" + "="*60)
    print("Examples completed! Check main.py for full implementation.")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
