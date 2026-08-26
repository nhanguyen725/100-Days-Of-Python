import random
from art import logo

def guess(choose_difficulty):
    attempts = -1
    if choose_difficulty == "easy":
        attempts = 10
    elif choose_difficulty == "hard":
        attempts = 5

    correct_guess = random.randint(1, 100)

    game_over = False

    while not game_over:

        print(f"You have {attempts} attempts remaining to guess the number.")

        if attempts == 0:
            game_over = True
            print("You've run out of guesses. Refresh the page to run again.")

        num = int(input("Make a guess: "))
        if num > correct_guess:
            print("Too high!\nGuess again.")
            attempts -= 1
        elif num < correct_guess:
            print("Too low!\nGuess again.")
            attempts -= 1
        elif num == correct_guess:
            game_over = True
            print("You guessed my number!")

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
guess(difficulty)


# if difficulty == "easy":
#     attempts = 10
#     print(f"You have {attempts} attempts remaining to guess the number.")
#     guess()
# elif difficulty == "hard":
#     attempts = 5
#     print(f"You have {attempts} attempts remaining to guess the number.")