# Password Generator

A beginner-friendly CLI program that generates secure passwords with customizable length and character types.

## Features

✓ **Generate Strong Passwords** - Creates passwords with uppercase, lowercase, numbers, and symbols
✓ **Custom Length** - User can specify the desired password length
✓ **Batch Generation** - Generate multiple passwords at once
✓ **Save to File** - Optionally save passwords to a text file with timestamps
✓ **Input Validation** - Ensures user enters valid values
✓ **User-Friendly Interface** - Clean, interactive CLI menu

## How to Use

### Running the Program

```bash
python main.py
```

### Menu Options

1. **Generate a single password**
   - Enter desired password length (minimum 8 characters)
   - Receives one strong password with all character types

2. **Generate multiple passwords**
   - Enter how many passwords to generate
   - Enter desired password length
   - Receives all passwords displayed in a formatted list

3. **Exit**
   - Closes the program

### Saving Passwords

After generating passwords, you'll be asked if you want to save them to a file. If you choose "y":
- Passwords are saved to `passwords.txt`
- Each save session includes a timestamp
- New saves are appended to existing content (never overwrites)

## Password Strength

Each generated password includes:
- **Uppercase letters** (A-Z)
- **Lowercase letters** (a-z)
- **Numbers** (0-9)
- **Symbols** (!@#$%^&*()_+-=[]{}|;:,.<>?)

The program guarantees at least one character from each type, then fills remaining positions with random characters from all types.

## Example Output

```
==================================================
WELCOME TO PASSWORD GENERATOR
==================================================

Choose an option:
1. Generate a single password
2. Generate multiple passwords
3. Exit

Enter your choice (1-3): 1
Enter password length (minimum 8): 16

==================================================
GENERATED PASSWORDS
==================================================
1. X$k9mLpQ2#aZvW4n
==================================================

Save to file? (y/n): y
✓ Passwords saved to 'passwords.txt'
```

## Files

- `main.py` - The main program file
- `README.md` - This file (documentation)
- `LEARNING_GUIDE.md` - Learning resources and concepts
- `passwords.txt` - Created automatically when you save passwords

## Requirements

- Python 3.6+
- Standard library only (no external dependencies needed)

## Learning Concepts

This program demonstrates:
- **Strings & Character Sets** - Using `string` module for character groups
- **Random Module** - `random.choice()` and `random.shuffle()`
- **Loops** - `while` loops for menu and `for` loops for generating multiple items
- **Functions** - Organizing code into reusable, documented functions
- **File I/O** - Reading and writing files
- **Error Handling** - Try/except for file operations and input validation
- **User Input** - Getting and validating user input
