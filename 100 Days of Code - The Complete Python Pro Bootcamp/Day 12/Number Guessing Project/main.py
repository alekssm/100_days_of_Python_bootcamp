import art
import random

difficulties = {
    "easy": 10,
    "hard": 5,
}

def print_attempts(attempts):
    print(f"You have {attempts} attempts remaining to guess the number.")

def make_a_guess():
    guess = int(input("Make a guess: "))
    return guess

def check_guess(number, guess):
    """Checks if guess is correct, if it is - returns 1, if it's not prints if it's
    too high or too low and returns 0"""
    if number == guess:
        return 1
    elif number < guess:
        print("Too high.")
    elif number > guess:
        print("Too low.")
    return 0

def play():
    hidden_number = random.randint(1, 100)

    success = False

    print(art.logo)
    print("\nWelcome to the number guessing game!")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    while difficulty != "easy" and difficulty!= "hard":
        difficulty = input("Invalid choice - Choose a difficulty. Type 'easy' or 'hard': ")

    attempts = difficulties[difficulty]

    while attempts > 0:
        print_attempts(attempts)
        is_found = check_guess(hidden_number, make_a_guess())
        if is_found == 1:
            success = True
            break
        else:
            attempts -= 1

    if success:
        print(f"You got it! Tha answer is {hidden_number}.")
    else:
        print("You've run out of guesses.")

play()
play_again = input("Guess another number? - 'y' or 'n'? ")
while play_again != "y" and play_again != "n":
    play_again = input("Invalid choice, type 'y' or 'n'? ")
    if play_again == "y":
        play()








