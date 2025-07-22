# We are going to write a program that generates a random number and asks the user to guess it.
# If the player’s guess is higher than the actual number, the program displays “Lower number please”.
#  Similarly, if the user’s guess is too low, the program prints “higher number please” 
# When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.




import random

def guess_the_number():
    while True:
        print("\n🎯 Welcome to 'Guess the Number' Game!")
        print("I'm thinking of a number between 1 and 100.")
        print("You have 10 chances to guess it!\n")

        number = random.randint(1, 100)
        max_attempts = 10
        attempts = 0
        user_input = None

        while attempts < max_attempts:
            try:
                user_input = int(input(f"Attempt {attempts + 1}/10 - Enter your guess: "))
            except ValueError:
                print("❌ Please enter a valid number!\n")
                continue

            attempts += 1

            if user_input > number:
                print("🔻 Lower number please!\n")
            elif user_input < number:
                print("🔺 Higher number please!\n")
            else:
                print(f"\n✅ You guessed it right! The number was {number}")
                print(f"📈 You took {attempts} attempts.\n")
                break
        else:
            print(f"\n❌ Game Over! You've used all 10 attempts.")
            print(f"The correct number was: {number}\n")

        play_again = input("🔁 Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("\n👋 Thanks for playing! See you next time.\n")
            break

guess_the_number()
