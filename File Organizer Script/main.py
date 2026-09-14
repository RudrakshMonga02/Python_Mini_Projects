import os
import shutil
from pathlib import Path


# File extension to category mapping
FILE_CATEGORIES = {
    'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.ico', '.webp'],
    'documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.xls', '.ppt', '.pptx', '.odt'],
    'videos': ['.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm', '.m4v'],
    'audio': ['.mp3', '.wav', '.aac', '.flac', '.m4a', '.wma', '.ogg'],
    'archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2']
}


def scan_directory(path):
    try:
        files = []
        # Loop through all items in the directory
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            # Only include files, not directories
            if os.path.isfile(item_path):
                files.append(item)
        return files
    except FileNotFoundError:
        print(f"Error: Directory '{path}' not found.")
        return []
    except PermissionError:
        print(f"Error: Permission denied to access '{path}'.")
        return []


def categorize_file(filename):
    # Get the file extension (in lowercase)
    file_extension = os.path.splitext(filename)[1].lower()
    
    # Loop through categories and check if extension matches
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension in extensions:
            return category
    
    # Return 'others' if no category matched
    return 'others'


def move_file(source, destination_folder):
    try:
        # Create destination folder if it doesn't exist
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
            print(f"Created folder: {destination_folder}")
        
        # Build the destination file path
        filename = os.path.basename(source)
        destination_path = os.path.join(destination_folder, filename)
        
        # Handle file name conflicts
        if os.path.exists(destination_path):
            name, extension = os.path.splitext(filename)
            counter = 1
            while os.path.exists(destination_path):
                new_filename = f"{name}_{counter}{extension}"
                destination_path = os.path.join(destination_folder, new_filename)
                counter += 1
        
        # Move the file
        shutil.move(source, destination_path)
        print(f"Moved: {filename} → {destination_folder}")
        return True
    except Exception as e:
        print(f"Error moving file {source}: {e}")
        return False


def organize_files(directory):
    print(f"\n{'='*50}")
    print(f"Starting file organization in: {directory}")
    print(f"{'='*50}\n")
    
    # Scan the directory for files
    files = scan_directory(directory)
    
    if not files:
        print("No files found in the directory.")
        return {'total': 0, 'organized': 0, 'failed': 0}
    
    print(f"Found {len(files)} file(s) to organize.\n")
    
    # Statistics
    stats = {'total': len(files), 'organized': 0, 'failed': 0}
    
    # Loop through each file and organize it
    for file in files:
        source_path = os.path.join(directory, file)
        
        # Skip directories
        if os.path.isdir(source_path):
            continue
        
        # Determine the category
        category = categorize_file(file)
        
        # Create the destination folder path
        destination_folder = os.path.join(directory, category)
        
        # Move the file to its category folder
        if move_file(source_path, destination_folder):
            stats['organized'] += 1
        else:
            stats['failed'] += 1
    
    # Print summary
    print(f"\n{'='*50}")
    print(f"Organization Complete!")
    print(f"{'='*50}")
    print(f"Total files: {stats['total']}")
    print(f"Organized: {stats['organized']}")
    print(f"Failed: {stats['failed']}")
    print(f"{'='*50}\n")
    
    return stats


def main():
    # Get the directory to organize (current directory by default)
    directory = input("Enter the directory path to organize (default: current directory): ").strip()
    
    if not directory:
        directory = os.getcwd()
    
    # Check if directory exists
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory.")
        return
    
    # Run the organization
    organize_files(directory)


if __name__ == "__main__":
    main()
