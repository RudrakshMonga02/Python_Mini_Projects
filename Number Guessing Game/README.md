# Number Guessing Game 🎮

A fun, interactive CLI game where you compete against the computer to guess a randomly selected number between 1 and 100.

## Features

✨ **Game Features:**
- Computer randomly selects a number between 1 and 100
- You have unlimited attempts to guess the number
- Real-time hints telling you if your guess is too high or too low
- Attempt counter to track how many guesses you needed
- Replay functionality to play multiple rounds
- Robust error handling for invalid input

## Requirements

- Python 3.6 or higher
- Standard library only (uses `random` module)

## How to Run

### Windows:
```bash
python main.py
```

### Linux/Mac:
```bash
python3 main.py
```

## How to Play

1. **Start the game** - The computer picks a number between 1-100
2. **Enter your guess** - Type a number and press Enter
3. **Read the hint** - You'll see if your guess is too high or too low
4. **Keep guessing** - Continue until you find the correct number
5. **Check your score** - See how many attempts it took you
6. **Play again** - Choose to play another round or quit

## Example Gameplay

```
🎮 Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Can you guess it?

Enter your guess (1-100): 50
⬇️  50 is too high. Try again!
Enter your guess (1-100): 25
⬆️  25 is too low. Try again!
Enter your guess (1-100): 37
⬆️  37 is too low. Try again!
Enter your guess (1-100): 43
🎉 Congratulations! You guessed the number: 43
📊 You took 4 attempts to win!

Do you want to play again? (yes/no): no

Thanks for playing! Goodbye! 👋
```

## Code Structure

### Main Functions

- **`generate_number()`** - Generates a random number 1-100
- **`get_user_guess()`** - Gets and validates user input
- **`check_guess()`** - Compares guess with secret number
- **`play_game()`** - Main game loop for one session
- **`main()`** - Entry point with replay logic

## Error Handling

The game handles various error scenarios:
- ✅ Non-numeric input → Asks for a valid number
- ✅ Out of range input → Requests number between 1-100
- ✅ Invalid replay response → Asks for "yes/no" clarification

## Learning Outcomes

This project demonstrates:
- **Loops** - `while` loops for game rounds and user input validation
- **Conditions** - `if/elif/else` statements for game logic and hints
- **Variables** - Tracking secret number, attempts, and game state
- **Error Handling** - Try/except blocks for input validation
- **Functions** - Modular code structure with clear responsibilities
- **String Methods** - `.lower()`, `.strip()` for input processing

## Tips for Winning

- 🎯 Start with 50 (best strategy to narrow down possibilities)
- 💡 Use binary search technique for optimal guesses
- 📊 Track which numbers you've already guessed
- 🧠 Pay attention to whether you need to go higher or lower
