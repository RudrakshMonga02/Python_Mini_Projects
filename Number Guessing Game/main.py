import random


def generate_number():
    return random.randint(1, 100)


def get_user_guess():
    while True:
        try:
            # Get input from user
            guess_input = input("Enter your guess (1-100): ")
            
            # Try to convert to integer
            guess = int(guess_input)
            
            # Validate range
            if guess < 1 or guess > 100:
                print("❌ Please enter a number between 1 and 100.")
                continue
            
            return guess
            
        except ValueError:
            # Handle non-numeric input
            print("❌ Invalid input! Please enter a valid number.")


def check_guess(secret_number, user_guess):
    if user_guess == secret_number:
        return "correct"
    elif user_guess > secret_number:
        return "too_high"
    else:
        return "too_low"


def play_game():
    # Generate the secret number
    secret_number = generate_number()
    attempts = 0
    guessed = False
    
    print("\n🎮 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it?\n")
    
    # Main game loop - continues until correct guess
    while not guessed:
        # Get user's guess
        user_guess = get_user_guess()
        attempts += 1
        
        # Check the guess and provide feedback
        result = check_guess(secret_number, user_guess)
        
        if result == "correct":
            # User guessed correctly
            guessed = True
            print(f"\n🎉 Congratulations! You guessed the number: {secret_number}")
            print(f"📊 You took {attempts} attempt{'s' if attempts != 1 else ''} to win!")
            
        elif result == "too_high":
            # Hint: guess is too high
            print(f"⬇️  {user_guess} is too high. Try again!")
            
        else:  # result == "too_low"
            # Hint: guess is too low
            print(f"⬆️  {user_guess} is too low. Try again!")


def main():
    play_again = True
    
    # Outer loop - allows replaying the game
    while play_again:
        play_game()
        
        # Ask if player wants to play again
        while True:
            replay_input = input("\nDo you want to play again? (yes/no): ").lower().strip()
            
            if replay_input in ["yes", "y"]:
                play_again = True
                break
            elif replay_input in ["no", "n"]:
                play_again = False
                print("\nThanks for playing! Goodbye! 👋\n")
                break
            else:
                print("❌ Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    main()
