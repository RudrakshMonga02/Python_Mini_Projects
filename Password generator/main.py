"""
Password Generator
A beginner-friendly CLI program that generates secure passwords.

Learning Focus:
- String module and character sets
- The random module (choice, shuffle)
- Loops and iteration
- Functions and return values
- File handling and I/O
- User input and validation
"""

import random
import string
import os
from datetime import datetime


def generate_password(length):
    """
    Generate a single strong password of the specified length.
    
    Args:
        length (int): The desired password length
        
    Returns:
        str: A randomly generated password with uppercase, lowercase, numbers, and symbols
    """
    # Define the character sets for a strong password
    uppercase = string.ascii_uppercase  # A-Z
    lowercase = string.ascii_lowercase  # a-z
    digits = string.digits  # 0-9
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Combine all character types
    all_characters = uppercase + lowercase + digits + symbols
    
    # Ensure at least one of each character type for strength
    password_chars = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(symbols)
    ]
    
    # Fill the rest with random characters
    for _ in range(length - 4):
        password_chars.append(random.choice(all_characters))
    
    # Shuffle the password to mix character types
    random.shuffle(password_chars)
    
    # Join the list into a string
    password = "".join(password_chars)
    
    return password


def generate_multiple(count, length):
    """
    Generate multiple passwords at once.
    
    Args:
        count (int): How many passwords to generate
        length (int): The length of each password
        
    Returns:
        list: A list of generated passwords
    """
    passwords = []
    for _ in range(count):
        password = generate_password(length)
        passwords.append(password)
    
    return passwords


def display_passwords(passwords):
    """
    Display passwords in a formatted way.
    
    Args:
        passwords (list): List of passwords to display
    """
    print("\n" + "="*50)
    print("GENERATED PASSWORDS")
    print("="*50)
    for i, password in enumerate(passwords, 1):
        print(f"{i}. {password}")
    print("="*50 + "\n")


def save_passwords(passwords, filename="passwords.txt"):
    """
    Save generated passwords to a file.
    
    Args:
        passwords (list): List of passwords to save
        filename (str): The filename to save to
    """
    try:
        # Open file in append mode (so we don't overwrite previous saves)
        with open(filename, "a") as file:
            # Write a header with timestamp
            file.write("\n")
            file.write("="*50 + "\n")
            file.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("="*50 + "\n")
            
            # Write each password
            for i, password in enumerate(passwords, 1):
                file.write(f"{i}. {password}\n")
        
        print(f"✓ Passwords saved to '{filename}'")
    except IOError as e:
        print(f"✗ Error saving passwords: {e}")


def get_valid_input(prompt, input_type=int, min_value=None):
    """
    Get valid user input with error handling.
    
    Args:
        prompt (str): The prompt to display
        input_type: The type to convert input to (int or str)
        min_value: Minimum value for integers
        
    Returns:
        The validated user input
    """
    while True:
        try:
            user_input = input(prompt)
            
            # Convert to the requested type
            if input_type == int:
                value = int(user_input)
                if min_value and value < min_value:
                    print(f"✗ Please enter a value of at least {min_value}")
                    continue
                return value
            else:
                return user_input
        
        except ValueError:
            print(f"✗ Invalid input. Please try again.")


def main():
    """
    Main function to run the password generator program.
    """
    print("\n" + "="*50)
    print("WELCOME TO PASSWORD GENERATOR")
    print("="*50 + "\n")
    
    while True:
        # Get user preferences
        print("Choose an option:")
        print("1. Generate a single password")
        print("2. Generate multiple passwords")
        print("3. Exit")
        print()
        
        choice = get_valid_input("Enter your choice (1-3): ")
        
        if choice == 1:
            # Generate single password
            length = get_valid_input("Enter password length (minimum 8): ", int, 8)
            password = generate_password(length)
            display_passwords([password])
            
            # Ask if user wants to save
            save_choice = input("Save to file? (y/n): ").lower()
            if save_choice == "y":
                save_passwords([password])
        
        elif choice == 2:
            # Generate multiple passwords
            count = get_valid_input("How many passwords to generate? (minimum 1): ", int, 1)
            length = get_valid_input("Enter password length (minimum 8): ", int, 8)
            
            passwords = generate_multiple(count, length)
            display_passwords(passwords)
            
            # Ask if user wants to save
            save_choice = input("Save to file? (y/n): ").lower()
            if save_choice == "y":
                save_passwords(passwords)
        
        elif choice == 3:
            print("\n✓ Thanks for using Password Generator!\n")
            break
        
        else:
            print("✗ Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
