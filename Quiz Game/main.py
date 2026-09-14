import random


def load_questions():
    """Load questions from a predefined list of dictionaries."""
    questions = [
        {
            "question": "What is the capital of France?",
            "answer": "Paris"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "answer": "Jupiter"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "answer": "William Shakespeare"
        },
        {
            "question": "What is the chemical symbol for gold?",
            "answer": "Au"
        },
        {
            "question": "In what year did the Titanic sink?",
            "answer": "1912"
        },
        {
            "question": "What is the smallest country in the world?",
            "answer": "Vatican City"
        },
        {
            "question": "How many continents are there?",
            "answer": "7"
        },
        {
            "question": "What is the speed of light?",
            "answer": "299792458 m/s"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "answer": "Leonardo da Vinci"
        },
        {
            "question": "What is the capital of Japan?",
            "answer": "Tokyo"
        }
    ]
    return questions


def ask_question(question_dict, question_number, total_questions):
    """
    Ask a single question and return True if the answer is correct.
    
    Args:
        question_dict: Dictionary containing "question" and "answer"
        question_number: Current question number
        total_questions: Total number of questions in the quiz
    
    Returns:
        bool: True if answer is correct, False otherwise
    """
    print(f"\n--- Question {question_number}/{total_questions} ---")
    print(question_dict["question"])
    
    user_answer = input("Your answer: ").strip()
    correct_answer = question_dict["answer"].strip()
    
    # Case-insensitive comparison
    if user_answer.lower() == correct_answer.lower():
        print("✓ Correct!")
        return True
    else:
        print(f"✗ Incorrect. The correct answer is: {correct_answer}")
        return False


def run_quiz():
    """Run the complete quiz game."""
    print("="*50)
    print("        Welcome to the Quiz Game!")
    print("="*50)
    
    # Load and randomize questions
    questions = load_questions()
    random.shuffle(questions)
    
    score = 0
    total_questions = len(questions)
    
    # Ask each question
    for i, question in enumerate(questions, 1):
        if ask_question(question, i, total_questions):
            score += 1
    
    # Show final results
    show_score(score, total_questions)


def show_score(score, total):
    """
    Display the final quiz results.
    
    Args:
        score: Number of correct answers
        total: Total number of questions
    """
    print("\n" + "="*50)
    print("                 QUIZ FINISHED!")
    print("="*50)
    print(f"Your Score: {score}/{total}")
    
    percentage = (score / total) * 100
    print(f"Percentage: {percentage:.1f}%")
    
    # Display performance message
    if percentage == 100:
        print("★ Perfect Score! Outstanding!")
    elif percentage >= 80:
        print("★ Excellent work!")
    elif percentage >= 60:
        print("★ Good job!")
    elif percentage >= 40:
        print("★ Nice effort!")
    else:
        print("★ Keep practicing!")
    
    print("="*50)


if __name__ == "__main__":
    run_quiz()
