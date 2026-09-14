# Contact Book Manager 📇

A simple Python CLI application to manage your personal contacts with full CRUD functionality.

## Features

- ✅ **Add Contact** - Add new contacts with name, phone, and email
- ✅ **Search Contact** - Search for contacts by name
- ✅ **View All Contacts** - Display all stored contacts
- ✅ **Delete Contact** - Remove contacts from your contact book
- ✅ **Persistent Storage** - Automatically saves and loads contacts from JSON file
- ✅ **Duplicate Prevention** - Prevents adding duplicate contact names

## Installation

1. Ensure you have Python 3.6+ installed
2. No external dependencies needed - uses only Python standard library (`json`)

## Usage

Run the application:

```bash
python main.py
```

### Menu Options

1. **Add Contact** - Add a new contact with name, phone number, and email
2. **Search Contact** - Find contacts by entering a partial or full name
3. **View All Contacts** - List all stored contacts with their details
4. **Delete Contact** - Remove a contact by name
5. **Exit** - Close the application (your data is automatically saved)

## Data Storage

- Contacts are stored in `contacts.json` in JSON format
- The file is automatically created on first use
- Data persists between sessions

## Example Contact Structure

```json
{
    "name": "John Doe",
    "phone": "555-0101",
    "email": "john@email.com"
}
```

## Sample Session

```
========================================
  CONTACT BOOK MANAGER
========================================
1. Add Contact
2. Search Contact
3. View All Contacts
4. Delete Contact
5. Exit
========================================
Enter your choice (1-5): 1

--- Add New Contact ---
Enter contact name: Alice Wonder
Enter phone number: 555-1234
Enter email address: alice@email.com
✓ Contact 'Alice Wonder' added successfully!
✓ Contacts saved successfully!
```

## Learning Concepts

This project demonstrates:
- **Dictionaries** - Contact data structure with key-value pairs
- **Lists** - Storing multiple contacts
- **File Handling** - Reading/writing JSON files
- **Functions** - Modular design with reusable functions
- **String Methods** - Input validation and case-insensitive search
- **Loops** - Menu loop and contact iteration
- **Conditionals** - Input validation and menu selection
