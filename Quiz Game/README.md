# Quiz Game

A command-line quiz game built with Python that tests your knowledge with randomized questions.

## Features

- **Randomized Questions**: Questions are shuffled in random order each time you play
- **Score Tracking**: Keeps track of correct and incorrect answers
- **Immediate Feedback**: Get instant feedback on whether your answer is correct
- **Final Results**: View your final score and performance rating
- **Case-Insensitive Answers**: Accepts answers regardless of capitalization

## How to Run

```bash
python main.py
```

## How to Play

1. Run the program
2. Read each question carefully
3. Type your answer and press Enter
4. Get immediate feedback on whether your answer is correct
5. After all questions, view your final score and performance rating

## Question Format

Questions are stored as dictionaries with the following format:

```python
{
    "question": "What is the capital of France?",
    "answer": "Paris"
}
```

## Performance Ratings

- **100%**: Perfect Score! Outstanding!
- **80% - 99%**: Excellent work!
- **60% - 79%**: Good job!
- **40% - 59%**: Nice effort!
- **Below 40%**: Keep practicing!

## Functions

- `load_questions()`: Loads the quiz questions from a predefined list
- `ask_question(question_dict, question_number, total_questions)`: Asks a single question and returns True if correct
- `run_quiz()`: Main function that runs the complete quiz game
- `show_score(score, total)`: Displays the final results and performance rating

## Example Output

```
==================================================
        Welcome to the Quiz Game!
==================================================

--- Question 1/10 ---
What is the capital of France?
Your answer: Paris
✓ Correct!

--- Question 2/10 ---
What is the largest planet in our solar system?
Your answer: Saturn
✗ Incorrect. The correct answer is: Jupiter

...

==================================================
                 QUIZ FINISHED!
==================================================
Your Score: 8/10
Percentage: 80.0%
★ Excellent work!
==================================================
```

## Technologies Used

- **Python 3.x**
- **Standard Library**: random module for shuffling questions

## Learning Topics

This project covers:

- **Lists**: Storing and iterating through collections of questions
- **Dictionaries**: Storing structured question data with keys
- **Loops**: Iterating through questions and displaying results
- **String Operations**: Converting answers to lowercase for comparison
- **Functions**: Modular code organization with single responsibilities
- **User Input**: Getting and processing user responses
