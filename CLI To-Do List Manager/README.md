# 📋 CLI To-Do List Manager

A command-line application for managing your daily tasks with persistent storage using JSON.

## Features

- ✅ **Add Tasks** - Create new tasks easily
- ✅ **Remove Tasks** - Delete tasks by their number
- ✅ **Mark Complete** - Toggle task completion status
- ✅ **View All Tasks** - See all tasks with their status
- ✅ **Persistent Storage** - Tasks are saved to `tasks.json` automatically
- ✅ **Auto-load** - Tasks are loaded when the program starts

## Installation

1. Make sure you have Python 3.x installed
2. Navigate to the project directory
3. Run the program:

```bash
python main.py
```

## Usage

When you run the program, you'll see a menu with options:

```
1. View all tasks       - Display all your tasks
2. Add a task          - Create a new task
3. Remove a task       - Delete an existing task
4. Mark task as complete/incomplete - Toggle task status
5. Exit                - Close the program
```

### Example Workflow

```
1. Choose option 2 to add a task
   Enter: "Study Python"

2. Choose option 2 again to add another task
   Enter: "Build a project"

3. Choose option 1 to view all tasks
   Output:
   1. [○ TODO] Study Python
   2. [○ TODO] Build a project

4. Choose option 4 to mark first task complete
   Enter task number: 1
   Output: "Task completed: 'Study Python'"

5. Choose option 1 to view tasks again
   Output:
   1. [✓ DONE] Study Python
   2. [○ TODO] Build a project
```

## Data Format

Tasks are stored in `tasks.json` with the following format:

```json
[
  {
    "task": "Study Python",
    "completed": true
  },
  {
    "task": "Build a project",
    "completed": false
  }
]
```

## Key Learning Concepts

This project demonstrates:

- **Lists**: Managing a collection of tasks
- **Dictionaries**: Storing task data (task name and completion status)
- **Loops**: Iterating through tasks and main program loop
- **Functions**: Organizing code into reusable functions
- **File I/O**: Reading and writing to JSON files
- **User Input**: Getting and validating user input
- **Error Handling**: Gracefully handling errors

## Functions Overview

| Function | Purpose |
|----------|---------|
| `load_tasks()` | Load tasks from JSON file |
| `save_tasks()` | Save tasks to JSON file |
| `show_tasks()` | Display all tasks |
| `add_task()` | Add a new task |
| `remove_task()` | Delete a task |
| `mark_complete()` | Toggle task completion |
| `main()` | Main program loop |

## Tips

- Tasks are automatically saved after each action
- You can mark a completed task as incomplete by selecting it again
- The program validates your input and shows helpful error messages
- Use Ctrl+C to exit if needed (though option 5 is recommended)
