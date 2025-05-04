import random
import hangman_art
import hangman_words

stages = hangman_art.stages

word_list = hangman_words.word_list
lives = 6

chosen_word = random.choice(word_list)

placeholder = list("_" * len(chosen_word))

print(hangman_art.logo)

guessed_letters = ""
while lives > 0:

    guess = input("Guess a letter: ").lower()
    if not guess.isalpha() or len(guess) != 1:
        print("Invalid choice - ", end="")
        continue

    if guess in guessed_letters:
        print("Already tried - ", end="")
        continue

    guessed_letters += guess

    correct = False
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            placeholder[i] = guess
            correct = True

    if correct:
        print(*placeholder)
        print("Right")
    else:
        lives -= 1
        print(*placeholder)
        print("Wrong")

    print(stages[lives])
    print(f"Lives left: {lives}\n")

    if "_" not in placeholder:
        break


if lives <=0:
    print(chosen_word)
    print(f"***********************YOU LOSE**********************")
    print("**************************** 0/6 LIVES LEFT****************************")

else:
    print(chosen_word)
    print("****************************YOU WIN****************************")
    print(f"**************************** {lives}/6 LIVES LEFT****************************")

