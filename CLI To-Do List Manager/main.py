"""
Command Line To-Do List Manager
A simple CLI application for managing your tasks with persistent storage using JSON.
"""

import json
import os


# File path where tasks will be stored
TASKS_FILE = "tasks.json"

# FILE I/O FUNCTIONS - Handle loading and saving tasks

def load_tasks():
    """
    Load tasks from the JSON file.
    Returns a list of task dictionaries.
    If the file doesn't exist, returns an empty list.
    """
    # Check if the tasks file exists
    if os.path.exists(TASKS_FILE):
        try:
            # Open the file and read the JSON data
            with open(TASKS_FILE, "r") as file:
                tasks = json.load(file)
                return tasks
        except (json.JSONDecodeError, IOError):
            # If there's an error reading the file, return empty list
            print("Warning: Could not read tasks file. Starting with empty list.")
            return []
    else:
        # File doesn't exist yet, return empty list
        return []

def save_tasks(tasks):
    """
    Save tasks to the JSON file.
    Accepts a list of task dictionaries and writes them to TASKS_FILE.
    """
    try:
        # Open file in write mode and save tasks as JSON with nice formatting
        with open(TASKS_FILE, "w") as file:
            json.dump(tasks, file, indent=2)
        print("✓ Tasks saved successfully!")
    except IOError:
        print("✗ Error: Could not save tasks to file.")

# TASK MANAGEMENT FUNCTIONS - Handle different task operations

def show_tasks(tasks):
    """
    Display all tasks with their status and index numbers.
    Shows task number, completion status, and task description.
    """
    # Check if there are any tasks
    if not tasks:
        print("\n📭 No tasks yet! Add one to get started.\n")
        return
    
    # Display header
    print("\n" + "=" * 60)
    print("YOUR TASKS")
    print("=" * 60)
    
    # Loop through tasks and display each one with its index
    for index, task in enumerate(tasks, 1):
        # Get the completion status - show emoji and text
        status = "✓ DONE" if task["completed"] else "○ TODO"
        
        # Display task with index, status, and description
        print(f"{index}. [{status}] {task['task']}")
    
    print("=" * 60 + "\n")


def add_task(tasks):
    """
    Add a new task to the list.
    Prompts user for task description and creates a new task dictionary.
    """
    # Get task description from user
    task_description = input("Enter a new task: ").strip()
    
    # Validate that task is not empty
    if not task_description:
        print("✗ Error: Task cannot be empty!\n")
        return
    
    # Create a new task dictionary with the description and incomplete status
    new_task = {
        "task": task_description,
        "completed": False
    }
    
    # Add the new task to the list
    tasks.append(new_task)
    print(f"✓ Task added: '{task_description}'\n")


def remove_task(tasks):
    """
    Remove a task from the list by its number.
    Prompts user for the task index and deletes it.
    """
    # First, show all tasks so user can see the numbers
    show_tasks(tasks)
    
    # Check if there are tasks to remove
    if not tasks:
        return
    
    try:
        # Get the task number from user
        task_number = int(input("Enter the task number to remove: "))
        
        # Convert to 0-based index (user enters 1-based numbers)
        index = task_number - 1
        
        # Validate that the index is within range
        if 0 <= index < len(tasks):
            # Store task name for confirmation message
            removed_task = tasks[index]["task"]
            # Remove the task at that index
            tasks.pop(index)
            print(f"✓ Task removed: '{removed_task}'\n")
        else:
            print(f"✗ Error: Task number must be between 1 and {len(tasks)}\n")
    except ValueError:
        # User didn't enter a valid number
        print("✗ Error: Please enter a valid number.\n")


def mark_complete(tasks):
    """
    Mark a task as completed by its number.
    Prompts user for the task index and toggles its completion status.
    """
    # First, show all tasks so user can see the numbers
    show_tasks(tasks)
    
    # Check if there are tasks to mark
    if not tasks:
        return
    
    try:
        # Get the task number from user
        task_number = int(input("Enter the task number to mark as complete: "))
        
        # Convert to 0-based index (user enters 1-based numbers)
        index = task_number - 1
        
        # Validate that the index is within range
        if 0 <= index < len(tasks):
            # Toggle the completion status
            tasks[index]["completed"] = not tasks[index]["completed"]
            
            # Show confirmation with new status
            status = "completed" if tasks[index]["completed"] else "marked as incomplete"
            print(f"✓ Task {status}: '{tasks[index]['task']}'\n")
        else:
            print(f"✗ Error: Task number must be between 1 and {len(tasks)}\n")
    except ValueError:
        # User didn't enter a valid number
        print("✗ Error: Please enter a valid number.\n")


# MAIN MENU AND PROGRAM FLOW

def show_menu():
    """Display the main menu options to the user."""
    print("\n" + "=" * 60)
    print("TO-DO LIST MANAGER")
    print("=" * 60)
    print("1. View all tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Mark task as complete/incomplete")
    print("5. Exit")
    print("=" * 60)


def main():
    """
    Main program loop.
    Displays menu, processes user input, and manages the program flow.
    """
    # Load existing tasks from file when program starts
    tasks = load_tasks()
    
    # Show welcome message
    print("\n🎯 Welcome to the To-Do List Manager!")
    
    # Main program loop - keeps running until user chooses to exit
    while True:
        # Display menu options
        show_menu()
        
        # Get user's choice
        choice = input("Choose an option (1-5): ").strip()
        
        # Process user's choice
        if choice == "1":
            # View all tasks
            show_tasks(tasks)
        
        elif choice == "2":
            # Add a new task
            add_task(tasks)
            save_tasks(tasks)
        
        elif choice == "3":
            # Remove a task
            remove_task(tasks)
            save_tasks(tasks)
        
        elif choice == "4":
            # Mark task as complete/incomplete
            mark_complete(tasks)
            save_tasks(tasks)
        
        elif choice == "5":
            # Exit the program
            print("\n👋 Thank you for using To-Do List Manager! Goodbye!\n")
            break
        
        else:
            # Invalid choice
            print("✗ Error: Please enter a valid option (1-5).\n")


# PROGRAM ENTRY POINT

if __name__ == "__main__":
    # Run the main program
    main()