# Quiz Game - Learning Guide

This guide explains the key concepts used in the Quiz Game project.

## Key Concepts

### 1. Lists

Lists are ordered collections that can store multiple items.

```python
questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 2 + 2?", "answer": "4"}
]
```

**Key operations:**
- `len(questions)` → Get the number of items
- `questions[0]` → Access first item
- `questions.append(item)` → Add an item
- `random.shuffle(questions)` → Randomize the order

### 2. Dictionaries

Dictionaries store data as key-value pairs, perfect for storing structured information.

```python
question_dict = {
    "question": "What is the capital of France?",
    "answer": "Paris"
}

# Access values
question_dict["question"]  # Returns the question
question_dict["answer"]    # Returns the answer
```

**Key operations:**
- `dictionary[key]` → Access a value
- `dictionary.get(key)` → Access with default fallback
- `for key in dictionary:` → Iterate through keys

### 3. Loops

Loops allow you to repeat actions for each item in a collection.

#### For Loop with enumerate()

```python
questions = [...]
for i, question in enumerate(questions, 1):
    # i = 1, 2, 3... (starting from 1)
    # question = each dictionary in the list
    print(f"Question {i}")
```

The `enumerate()` function:
- Returns both the index and value
- `enumerate(questions, 1)` starts counting from 1 instead of 0

#### While Loop

```python
answered_count = 0
while answered_count < total_questions:
    # Ask question
    answered_count += 1
```

### 4. String Methods

Used for processing user input:

```python
user_input = input("Your answer: ")

user_input.strip()           # Remove leading/trailing spaces
user_input.lower()           # Convert to lowercase
user_input.upper()           # Convert to uppercase
user_input.capitalize()      # Capitalize first letter
```

### 5. Functions

Functions organize code into reusable blocks.

```python
def load_questions():
    """Load questions from a predefined list of dictionaries."""
    questions = [...]
    return questions

# Function call
all_questions = load_questions()
```

**Function benefits:**
- **DRY Principle**: Don't Repeat Yourself
- **Readability**: Clear intent via function name
- **Testability**: Easier to test individual parts
- **Reusability**: Use same function multiple times

### 6. Module: random

The `random` module provides functions for randomization.

```python
import random

# Shuffle a list in place (modifies the original list)
random.shuffle(my_list)

# Get a random item from a list
random.choice(my_list)

# Get random number between 0 and 1
random.random()

# Get random integer in range
random.randint(1, 100)
```

## How the Quiz Game Works

### Step 1: Load Questions
```python
questions = load_questions()  # Get list of dictionaries
```

### Step 2: Randomize Order
```python
random.shuffle(questions)     # Change the order randomly
```

### Step 3: Loop Through Questions
```python
for i, question in enumerate(questions, 1):
    # Each iteration processes one question
    ask_question(question, i, total_questions)
```

### Step 4: Track Score
```python
score = 0
if ask_question(...):        # Returns True if correct
    score += 1               # Increment score
```

### Step 5: Show Results
```python
show_score(score, total)     # Display final results
```

## Practice Exercises

### Exercise 1: Add More Questions
Add 5 more questions to the `load_questions()` function.

```python
{
    "question": "Your question here?",
    "answer": "Your answer here"
}
```

### Exercise 2: Difficulty Levels
Modify the program to ask users to select a difficulty level, then filter questions by difficulty.

**Hint**: Add a "difficulty" key to each question dictionary.

### Exercise 3: Save High Scores
Store the highest score achieved in a file.

**Hint**: Use `open()` and `write()` to save scores.

### Exercise 4: Time Limit
Add a time limit for answering each question.

**Hint**: Use the `time` module with `time.time()`

### Exercise 5: Question Categories
Organize questions by category (e.g., "History", "Science", "Geography").

**Hint**: Add a "category" key to each question dictionary.

## Common Mistakes to Avoid

### 1. Not Removing Whitespace
```python
# ✗ Wrong: Spaces can cause comparison to fail
user_answer = input("Your answer: ")

# ✓ Correct: Remove leading/trailing spaces
user_answer = input("Your answer: ").strip()
```

### 2. Case-Sensitive Comparison
```python
# ✗ Wrong: "paris" != "Paris"
if user_answer == correct_answer:

# ✓ Correct: Both converted to lowercase
if user_answer.lower() == correct_answer.lower():
```

### 3. Modifying List While Iterating
```python
# ✗ Wrong: Can skip items
for item in my_list:
    my_list.remove(item)

# ✓ Correct: Iterate through a copy
for item in my_list.copy():
    my_list.remove(item)
```

### 4. Forgetting to Return Values
```python
# ✗ Wrong: Function doesn't return anything
def ask_question(question_dict):
    if user_answer == correct_answer:
        print("Correct!")
    # Missing return statement

# ✓ Correct: Function returns the result
def ask_question(question_dict):
    if user_answer == correct_answer:
        print("Correct!")
        return True
    return False
```

## Key Takeaways

1. **Lists** store multiple items and support operations like shuffling
2. **Dictionaries** organize data with meaningful keys
3. **Loops** automate repetitive tasks like asking each question
4. **String methods** help process user input consistently
5. **Functions** make code organized, readable, and reusable
6. The **random module** adds unpredictability to make quizzes interesting

## Next Steps

- Modify the code to add new features (see exercises)
- Experiment with different question types
- Combine this with file I/O to save questions to a JSON file
- Create a web version using Flask or Django
