import pandas as pd

nato_alphabet_df = pd.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter:row.code for index, row in nato_alphabet_df.iterrows()}

def test_input():
    try:
        user_word = input("Write a word: ").upper()
        hidden_word = [nato_alphabet[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet, please!")
        test_input()
    else:
        print(hidden_word)


test_input()


