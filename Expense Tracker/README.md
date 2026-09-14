# Expense Tracker CLI

A command-line application to track personal expenses with categories, persistent storage, and spending analytics.

## Features

✅ **Add Expenses** - Record expenses with amount, category, and description  
✅ **View Expenses** - Display all recorded expenses in a formatted table  
✅ **Track Spending** - Calculate total spending and breakdown by category  
✅ **Category Support** - Predefined categories (food, travel, utilities, etc.) or custom  
✅ **Persistent Storage** - Save/load expenses from JSON file  
✅ **Delete Expenses** - Remove individual expense records  
✅ **Timestamps** - Automatic date/time recording for each expense

## Quick Start

```bash
python main.py
```

## Menu Options

```
1. Add expense       - Create a new expense record
2. View expenses     - Display all expenses in table format
3. Show total        - View spending summary and category breakdown
4. Delete expense    - Remove an expense from the records
5. Exit              - Save and exit the application
```

## Example Usage

### Adding an Expense
```
Select an option: 1
Enter amount: 25.50
Select category:
  1. food
  2. travel
  ...
  7. other
Select category: 1
Enter description: Lunch at cafe
✓ Expense added: $25.50 - Food
```

### Viewing All Expenses
```
Select an option: 2
======= ALL EXPENSES =======
Date                 Category        Amount       Description
2024-01-15 12:30:45  Food            $25.50       Lunch at cafe
2024-01-15 14:20:10  Travel          $15.00       Bus fare
```

### Viewing Total Spending
```
Select an option: 3
======= SPENDING SUMMARY =======
Total Spending: $40.50

Breakdown by Category:
  Food                     $25.50 (62.9%)
  Travel                   $15.00 (37.1%)
```

## Data Storage

Expenses are automatically saved to `expenses.json`:

```json
[
  {
    "amount": 25.50,
    "category": "food",
    "description": "Lunch at cafe",
    "date": "2024-01-15 12:30:45"
  },
  {
    "amount": 15.00,
    "category": "travel",
    "description": "Bus fare",
    "date": "2024-01-15 14:20:10"
  }
]
```

## Learning Concepts

This project teaches:

- **Lists**: Storing multiple expense records
- **Dictionaries**: Structuring expense data (amount, category, description, date)
- **File Handling**: Reading/writing JSON files using the `json` module
- **String Formatting**: Creating formatted output tables
- **Error Handling**: Input validation and exception handling
- **Loops & Control Flow**: Menu-driven application logic
- **Functions**: Modular code organization

## Functions Reference

| Function | Purpose |
|----------|---------|
| `load_expenses()` | Load expenses from JSON file |
| `save_expenses(expenses)` | Save expenses to JSON file |
| `add_expense(expenses)` | Add a new expense to the list |
| `view_expenses(expenses)` | Display all expenses |
| `calculate_total(expenses)` | Show total and category breakdown |
| `delete_expense(expenses)` | Remove an expense |
| `main()` | Main application loop |

## Requirements

- Python 3.6+
- Standard Library (no external dependencies)
  - `json` - for file handling
  - `os` - for file path checking
  - `datetime` - for timestamps

## Tips

1. **Validate Input**: The app validates amounts and category selections
2. **Custom Categories**: Enter your own category name when prompted
3. **Data Persistence**: All changes are automatically saved to `expenses.json`
4. **No Internet Required**: Everything is local and offline
5. **Easy Backup**: Simply copy `expenses.json` to backup your data

## Troubleshooting

**"Corrupted file" error**: Delete the `expenses.json` file and restart  
**Invalid input**: Enter data in the correct format (numbers for amounts, etc.)  
**No expenses showing**: The app starts fresh if `expenses.json` is missing

## Future Enhancements

- Export to CSV
- Filter by date range
- Monthly/weekly reports
- Budget limits and alerts
- Edit existing expenses
- Multiple user profiles
