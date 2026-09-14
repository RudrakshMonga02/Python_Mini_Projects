import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Load contacts from JSON file. Returns an empty list if file doesn't exist."""
    if os.path.exists(CONTACTS_FILE):
        try:
            with open(CONTACTS_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []

def save_contacts(contacts):
    """Save contacts to JSON file."""
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)
    print("✓ Contacts saved successfully!")

def add_contact(contacts):
    """Add a new contact to the contacts list."""
    print("\n--- Add New Contact ---")
    name = input("Enter contact name: ").strip()
    
    # Check if contact already exists
    if any(contact["name"].lower() == name.lower() for contact in contacts):
        print("✗ Contact with this name already exists!")
        return
    
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    
    # Add new contact
    new_contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    
    contacts.append(new_contact)
    save_contacts(contacts)
    print(f"✓ Contact '{name}' added successfully!")

def search_contact(contacts):
    """Search for a contact by name."""
    print("\n--- Search Contact ---")
    search_term = input("Enter contact name to search: ").strip().lower()
    
    results = [contact for contact in contacts if search_term in contact["name"].lower()]
    
    if results:
        print(f"\n✓ Found {len(results)} contact(s):")
        for contact in results:
            print(f"\n  Name:  {contact['name']}")
            print(f"  Phone: {contact['phone']}")
            print(f"  Email: {contact['email']}")
    else:
        print("✗ No contacts found matching your search.")

def delete_contact(contacts):
    """Delete a contact by name."""
    print("\n--- Delete Contact ---")
    name_to_delete = input("Enter contact name to delete: ").strip()
    
    # Find and remove the contact
    for i, contact in enumerate(contacts):
        if contact["name"].lower() == name_to_delete.lower():
            removed = contacts.pop(i)
            save_contacts(contacts)
            print(f"✓ Contact '{removed['name']}' deleted successfully!")
            return
    
    print("✗ Contact not found.")

def show_contacts(contacts):
    """Display all contacts."""
    print("\n--- All Contacts ---")
    
    if not contacts:
        print("No contacts stored yet.")
        return
    
    print(f"\nTotal contacts: {len(contacts)}\n")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. Name:  {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}")
        print()

def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 40)
    print("  CONTACT BOOK MANAGER")
    print("=" * 40)
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. View All Contacts")
    print("4. Delete Contact")
    print("5. Exit")
    print("=" * 40)
    return input("Enter your choice (1-5): ").strip()

def main():
    """Main program loop."""
    # Load existing contacts on startup
    contacts = load_contacts()
    print("✓ Contacts loaded on startup!")
    
    while True:
        choice = display_menu()
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            show_contacts(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("\nThank you for using Contact Book Manager. Goodbye!")
            break
        else:
            print("✗ Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
