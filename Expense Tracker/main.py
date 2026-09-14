import json
import os
from datetime import datetime


# File to store expenses
EXPENSES_FILE = "expenses.json"


def load_expenses():
    """
    Load expenses from JSON file.
    
    Returns:
        list: List of expense dictionaries, empty list if file doesn't exist
    """
    if os.path.exists(EXPENSES_FILE):
        try:
            with open(EXPENSES_FILE, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Warning: Corrupted file. Starting fresh.")
            return []
    return []


def save_expenses(expenses):

    try:
        with open(EXPENSES_FILE, 'w') as file:
            json.dump(expenses, file, indent=2)
        print("✓ Expenses saved successfully!")
    except Exception as e:
        print(f"Error saving expenses: {e}")


def add_expense(expenses):
    try:
        # Get amount
        while True:
            try:
                amount = float(input("Enter amount: $"))
                if amount <= 0:
                    print("Amount must be positive!")
                    continue
                break
            except ValueError:
                print("Invalid amount. Please enter a number.")
        
        # Display available categories
        categories = ["food", "travel", "utilities", "entertainment", 
                     "health", "shopping", "other"]
        print("\nAvailable categories:")
        for i, cat in enumerate(categories, 1):
            print(f"  {i}. {cat}")
        
        # Get category choice
        while True:
            try:
                choice = int(input("Select category (1-7) or enter custom: "))
                if 1 <= choice <= len(categories):
                    category = categories[choice - 1]
                    break
                else:
                    print(f"Please enter a number between 1 and {len(categories)}")
            except ValueError:
                category = input("Enter custom category: ").strip().lower()
                if category:
                    break
                print("Category cannot be empty!")
        
        # Get description
        description = input("Enter description: ").strip()
        if not description:
            description = "No description"
        
        # Create expense dictionary
        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Add to expenses list
        expenses.append(expense)
        print(f"\n✓ Expense added: ${amount:.2f} - {category.capitalize()}")
        
    except Exception as e:
        print(f"Error adding expense: {e}")


def view_expenses(expenses):
    if not expenses:
        print("\nNo expenses recorded yet!")
        return
    
    print("\n" + "=" * 70)
    print("ALL EXPENSES")
    print("=" * 70)
    print(f"{'Date':<20} {'Category':<15} {'Amount':<12} {'Description':<20}")
    print("-" * 70)
    
    for expense in expenses:
        date = expense.get("date", "N/A")
        category = expense["category"].capitalize()
        amount = f"${expense['amount']:.2f}"
        description = expense["description"][:19]
        print(f"{date:<20} {category:<15} {amount:<12} {description:<20}")
    
    print("=" * 70)


def calculate_total(expenses):
    if not expenses:
        print("\nNo expenses to calculate!")
        return
    
    total = 0
    category_totals = {}
    
    # Calculate totals
    for expense in expenses:
        amount = expense["amount"]
        category = expense["category"]
        total += amount
        
        if category not in category_totals:
            category_totals[category] = 0
        category_totals[category] += amount
    
    # Display results
    print("\n" + "=" * 50)
    print("SPENDING SUMMARY")
    print("=" * 50)
    print(f"Total Spending: ${total:.2f}")
    print("\nBreakdown by Category:")
    print("-" * 50)
    
    for category in sorted(category_totals.keys()):
        amount = category_totals[category]
        percentage = (amount / total) * 100
        print(f"  {category.capitalize():<20} ${amount:>8.2f} ({percentage:>5.1f}%)")
    
    print("=" * 50)


def delete_expense(expenses):
    if not expenses:
        print("\nNo expenses to delete!")
        return
    
    view_expenses(expenses)
    
    try:
        index = int(input("\nEnter expense number to delete (1-based): ")) - 1
        if 0 <= index < len(expenses):
            deleted = expenses.pop(index)
            print(f"✓ Deleted: ${deleted['amount']:.2f} - {deleted['category']}")
        else:
            print("Invalid expense number!")
    except ValueError:
        print("Please enter a valid number!")


def show_menu():
    """Display the main menu options."""
    print("\n" + "=" * 50)
    print("EXPENSE TRACKER")
    print("=" * 50)
    print("1. Add expense")
    print("2. View all expenses")
    print("3. Show total spending")
    print("4. Delete expense")
    print("5. Exit")
    print("=" * 50)


def main():
    print("\nWelcome to Expense Tracker!")
    
    # Load existing expenses
    expenses = load_expenses()
    if expenses:
        print(f"Loaded {len(expenses)} expense(s) from file.")
    
    while True:
        show_menu()
        choice = input("Select an option (1-5): ").strip()
        
        if choice == "1":
            add_expense(expenses)
            save_expenses(expenses)
        
        elif choice == "2":
            view_expenses(expenses)
        
        elif choice == "3":
            calculate_total(expenses)
        
        elif choice == "4":
            delete_expense(expenses)
            save_expenses(expenses)
        
        elif choice == "5":
            if expenses:
                save_expenses(expenses)
            print("\nGoodbye!")
            break
        
        else:
            print("Invalid option! Please select 1-5.")


if __name__ == "__main__":
    main()
