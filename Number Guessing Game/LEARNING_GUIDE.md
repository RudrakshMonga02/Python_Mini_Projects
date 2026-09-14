# Learning Guide - Number Guessing Game

This guide explains the programming concepts demonstrated in the Number Guessing Game.

## 📚 Learning Concepts

### 1. **Loops** 🔄

Loops allow code to repeat until a condition is met.

#### `while` Loop - Game Loop
```python
while not guessed:
    user_guess = get_user_guess()
    attempts += 1
    result = check_guess(secret_number, user_guess)
    if result == "correct":
        guessed = True
```
- **Purpose**: Repeats guessing until user finds the correct number
- **Condition**: `not guessed` continues until `guessed` becomes `True`
- **Key Learning**: Exit conditions must eventually become true

#### `while` Loop - Input Validation
```python
while True:
    try:
        guess_input = input("Enter your guess (1-100): ")
        guess = int(guess_input)
        if guess < 1 or guess > 100:
            print("❌ Please enter a number between 1 and 100.")
            continue
        return guess
    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")
```
- **Purpose**: Keeps asking for input until valid answer received
- **Key Learning**: `break` exits loop, `continue` skips to next iteration
- **Pattern**: Ask → Validate → Either return or ask again

#### `while` Loop - Replay Option
```python
while play_again:
    play_game()
    # Ask if they want to play again
```
- **Purpose**: Allows multiple game sessions without restarting program
- **Key Learning**: Same loop can control different behaviors

---

### 2. **Conditions** ❓

Conditions use `if`, `elif`, and `else` to make decisions.

#### Comparison in Game Logic
```python
def check_guess(secret_number, user_guess):
    if user_guess == secret_number:
        return "correct"
    elif user_guess > secret_number:
        return "too_high"
    else:
        return "too_low"
```
- **`==`** : Check if values are **equal**
- **`>`** : Check if left is **greater than** right
- **`<`** : Check if left is **less than** right
- **Flow**: First true condition executes, rest are skipped

#### Range Validation
```python
if guess < 1 or guess > 100:
    print("❌ Please enter a number between 1 and 100.")
    continue
```
- **`or`** : True if **either** condition is true
- **`and`** : True if **both** conditions are true
- **`not`** : Reverses boolean value (True → False, False → True)

#### Boolean Tracking
```python
guessed = False  # Start: game not won
# ... game loop ...
if result == "correct":
    guessed = True  # End condition met
```
- **Purpose**: Use boolean variables as flags to control loop flow
- **Key Learning**: `True`/`False` are actual boolean values in Python

---

### 3. **Variables** 📝

Variables store data that can change during program execution.

#### State Variables (Track Game Progress)
```python
secret_number = generate_number()  # Computer's number
attempts = 0                        # How many tries so far
guessed = False                     # Has user won?
```

#### Changing Variables
```python
attempts += 1  # Increment: attempts = attempts + 1
```
- **`+=`** : Add to existing value
- **`-=`** : Subtract from existing value
- **`*=`** : Multiply existing value
- **`/=`** : Divide existing value

#### Naming Variables
```python
# ✅ Good: Clear, describes purpose
user_guess = 42
secret_number = 75
replay_input = "yes"

# ❌ Bad: Unclear, vague
x = 42  # What is x?
n = 75  # What does n mean?
resp = "yes"  # Too abbreviated
```

#### Variable Scope
```python
def play_game():
    secret_number = generate_number()  # Local to this function
    # Can use secret_number here
    
# secret_number not accessible here - it's local to play_game()
```

---

### 4. **Error Handling** ⚠️

Error handling prevents crashes when unexpected input occurs.

#### Try/Except Block
```python
try:
    guess_input = input("Enter your guess (1-100): ")
    guess = int(guess_input)  # Could fail if input is text
    
except ValueError:  # Catches conversion errors
    print("❌ Invalid input! Please enter a valid number.")
```

**What happens:**
1. Code in `try` block runs normally
2. If ValueError occurs (e.g., `int("hello")` fails), jump to `except`
3. Handle the error gracefully instead of crashing

#### Multiple Error Checks
```python
while True:
    try:
        guess = int(guess_input)
        
        if guess < 1 or guess > 100:  # Logical check
            print("❌ Please enter a number between 1 and 100.")
            continue
        
        return guess
        
    except ValueError:  # Handles type error
        print("❌ Invalid input! Please enter a valid number.")
```

**Two types of validation:**
1. **Try/Except** - Catches unexpected data types
2. **If Statement** - Checks logical constraints (range)

---

### 5. **Functions** 🎯

Functions group code into reusable blocks.

#### Function Definition
```python
def function_name(parameters):
    """Docstring explaining what function does"""
    # Function body
    return result
```

#### Example: Check Guess Assessment
```python
def check_guess(secret_number, user_guess):
    """
    Compare guess with secret number.
    
    Args:
        secret_number (int): Computer's number
        user_guess (int): Player's guess
    
    Returns:
        str: "correct", "too_high", or "too_low"
    """
    if user_guess == secret_number:
        return "correct"
    elif user_guess > secret_number:
        return "too_high"
    else:
        return "too_low"
```

**Benefits:**
- ✅ Reusable - called multiple times in game
- ✅ Readable - clear what it does
- ✅ Testable - can verify it works correctly
- ✅ Maintainable - change logic in one place

#### Return Values
```python
def generate_number():
    return random.randint(1, 100)  # Returns a value

secret_number = generate_number()  # Stores returned value
```

#### Parameters vs Arguments
```python
def check_guess(secret_number, user_guess):  # Parameters (defined)
    # function body

check_guess(42, 50)  # Arguments (passed in)
```

---

## 🧩 How It All Works Together

```
main()
  ├─ Loop: play_again = True
  │    └─ play_game()
  │         ├─ secret_number = generate_number()
  │         ├─ attempts = 0, guessed = False
  │         └─ Loop: while not guessed
  │              ├─ user_guess = get_user_guess()
  │              │    └─ Loop: until valid input
  │              │         └─ Try/Except for conversion
  │              │         └─ If for range check
  │              ├─ attempts += 1
  │              ├─ result = check_guess()
  │              │    └─ If/Elif/Else for comparison
  │              └─ If result == "correct": guessed = True
  │    └─ Ask: replay_input = get replay choice
  │         └─ If/Elif/Else to set play_again
```

---

## 💡 Key Programming Patterns

### Pattern 1: Input Validation Loop
```python
while True:
    try:
        user_input = get_input()  # Try to get input
        validate(user_input)      # Check if valid
        break                      # Exit if valid
    except:
        print("Try again")         # Ask again if invalid
```

### Pattern 2: Game Loop
```python
game_active = True
while game_active:
    # Get player action
    # Update game state
    # Check win/lose condition
    # If player won/lost: game_active = False
```

### Pattern 3: Binary Comparison
```python
if value == target:
    return "equal"
elif value > target:
    return "greater"
else:
    return "less"
```

---

## 🎯 Common Mistakes to Avoid

1. **Infinite Loop**
   ```python
   # ❌ Wrong: Condition never becomes false
   while True:
       print("Hello")
   
   # ✅ Correct: Include exit condition
   attempts = 0
   while attempts < 3:
       print("Hello")
       attempts += 1
   ```

2. **Forgetting Return Value**
   ```python
   # ❌ Wrong: Function doesn't return anything
   def get_number():
       number = 42
   
   result = get_number()  # result is None
   
   # ✅ Correct: Use return statement
   def get_number():
       number = 42
       return number
   ```

3. **Not Handling Exceptions**
   ```python
   # ❌ Wrong: Program crashes on invalid input
   guess = int(input("Guess: "))
   
   # ✅ Correct: Catch potential error
   try:
       guess = int(input("Guess: "))
   except ValueError:
       print("Please enter a number")
   ```

4. **Comparing with `=` instead of `==`**
   ```python
   # ❌ Wrong: Assignment, not comparison
   if guess = 50:
       print("Equal")
   
   # ✅ Correct: Use == for comparison
   if guess == 50:
       print("Equal")
   ```

---

## 📊 Exercises to Deepen Learning

1. **Add difficulty levels** - Easy (1-50), Hard (1-200)
2. **Add a hint system** - Player can ask for hints (limited)
3. **Track best scores** - Save attempts to a file
4. **Add AI opponent** - Computer also guesses a number
5. **Add statistics** - Show average attempts, win rate
6. **Modify range** - Let user choose the range

---

## 🔍 Testing the Code

Test various scenarios:

```python
# Test 1: Normal gameplay
# Input: 50, 25, 37, 40, 42 (assuming secret is 42)
# Expected: 5 attempts, correct guess

# Test 2: Error handling
# Input: "hello", "abc", "50"
# Expected: Error messages, then accept "50"

# Test 3: Edge cases
# Input: 1 (first attempt)
# Input: 100 (last attempt)
# Expected: Game accepts valid range

# Test 4: Replay
# Finish game, type "yes", verify new game starts
# Finish game, type "no", verify program exits
```

---

## 📖 Additional Resources

- Python official docs: https://docs.python.org/3/
- `random` module: https://docs.python.org/3/library/random.html
- Exception Handling: https://docs.python.org/3/tutorial/errors.html
- Functions: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
