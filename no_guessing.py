import random

def play_game(l,u):
    print("\n Welcome to the Number Guessing Game!")
    lower = l
    upper = u
    number_to_guess = random.randint(lower, upper)
    max_attempts = int(input("enter number of do you want to guess the correct number:"))
    attempts = 0

    print(f"I'm thinking of a number between {lower} and {upper}.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}: Enter your guess: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        attempts += 1

        if guess == number_to_guess:
            print(f"🎉 Correct! You guessed the number in {attempts} attempt(s).")
            break
        elif guess < number_to_guess:
            print("🔼 Too low! Try a higher number.")
        else:
            print("🔽 Too high! Try a lower number.")

    else:
        print(f"\n💥 Game Over! The correct number was {number_to_guess}.")

def main():
    while True:
        o=int(input("enter the lower bounded number:\t"))
        p=int(input("\nenter the upper bounded number:\t"))
        play_game(o,p)
        again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("👋 Thanks for playing! Goodbye.")
            break

main()
