"""
Random Nickname Generator
A beginner-friendly CLI program that generates random nicknames.

Learning Focus:
- Lists and dictionaries
- Functions and return values
- File handling (JSON)
- Loops and user input
- Error handling
- The random module
"""

import json
import os
import random


# File where we'll store nicknames
DATA_FILE = "nicknames.json"


def load_nicknames():
    """
    Load nicknames from a JSON file.
    
    Returns:
        list: A list of nicknames. If the file doesn't exist, returns a default list.
    """
    # Check if the file exists
    if os.path.exists(DATA_FILE):
        try:
            # Open and read the JSON file
            with open(DATA_FILE, "r") as file:
                nicknames = json.load(file)
                print(f"✓ Loaded {len(nicknames)} nicknames from file.\n")
                return nicknames
        except json.JSONDecodeError:
            # If the file is corrupted, start fresh with defaults
            print("⚠ File was corrupted. Starting fresh with default nicknames.\n")
            return get_default_nicknames()
    else:
        # File doesn't exist yet, use defaults
        print("✓ Starting with default nicknames.\n")
        return get_default_nicknames()


def get_default_nicknames():
    """
    Provide a default list of cute nicknames for beginners.
    
    Returns:
        list: Default list of nicknames
    """
    return [
        "Sunny",
        "Pixel",
        "Tiger",
        "Marble",
        "Nova",
        "Buddy",
        "Echo",
        "Comet",
        "Wise",
        "Spark",
        "Luna",
        "Jazz",
        "Pepper",
        "Shadow",
        "Cloud",
    ]


def save_nicknames(nicknames):
    """
    Save nicknames to a JSON file.
    
    Args:
        nicknames (list): The list of nicknames to save
    """
    try:
        # Open the file in write mode and save as JSON
        with open(DATA_FILE, "w") as file:
            json.dump(nicknames, file, indent=2)
        print(f"✓ Saved {len(nicknames)} nicknames to file.\n")
    except IOError as error:
        # Handle file write errors
        print(f"✗ Error saving file: {error}\n")


def get_random_nickname(nicknames):
    """
    Pick a random nickname from the list.
    
    Args:
        nicknames (list): List of available nicknames
        
    Returns:
        str: A randomly selected nickname
    """
    # Use random.choice() to pick one item from the list
    return random.choice(nicknames)


def add_nickname(nicknames):
    """
    Ask the user to add a new nickname to the list.
    
    Args:
        nicknames (list): The existing list of nicknames
        
    Returns:
        list: The updated list with the new nickname (if added)
    """
    # Get input from the user
    new_nickname = input("Enter a new nickname: ").strip()
    
    # Check if the input is empty
    if not new_nickname:
        print("✗ Nickname cannot be empty. Try again.\n")
        return nicknames
    
    # Check if the nickname already exists
    if new_nickname in nicknames:
        print(f"✗ '{new_nickname}' already exists in the list.\n")
        return nicknames
    
    # Add the new nickname to the list
    nicknames.append(new_nickname)
    print(f"✓ Added '{new_nickname}' to the list!\n")
    return nicknames


def display_menu():
    """
    Display the main menu options.
    """
    print("\n" + "=" * 40)
    print("  Random Nickname Generator")
    print("=" * 40)
    print("1. Generate a random nickname")
    print("2. Add a new nickname")
    print("3. View all nicknames")
    print("4. Exit")
    print("=" * 40 + "\n")


def view_all_nicknames(nicknames):
    """
    Display all available nicknames.
    
    Args:
        nicknames (list): List of all nicknames
    """
    print("\n--- All Nicknames ---")
    for index, nickname in enumerate(nicknames, start=1):
        print(f"{index}. {nickname}")
    print()


def main():
    """
    Main program loop. Runs the entire application.
    """
    # Load nicknames from file when program starts
    nicknames = load_nicknames()
    
    # Keep the program running with a while loop
    while True:
        display_menu()
        
        # Get user's choice
        choice = input("Choose an option (1-4): ").strip()
        
        # Option 1: Generate a random nickname
        if choice == "1":
            random_name = get_random_nickname(nicknames)
            print(f"\n🎲 Your random nickname is: {random_name}\n")
        
        # Option 2: Add a new nickname
        elif choice == "2":
            print()
            nicknames = add_nickname(nicknames)
            # Save the updated list to file
            save_nicknames(nicknames)
        
        # Option 3: View all nicknames
        elif choice == "3":
            view_all_nicknames(nicknames)
        
        # Option 4: Exit the program
        elif choice == "4":
            print("👋 Thanks for using Random Nickname Generator. Goodbye!\n")
            break
        
        # Handle invalid input
        else:
            print("✗ Invalid choice. Please enter 1, 2, 3, or 4.\n")


# Run the program when this file is executed
if __name__ == "__main__":
    main()
