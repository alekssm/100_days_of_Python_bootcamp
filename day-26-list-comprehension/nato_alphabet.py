import pandas as pd

nato_alphabet_df = pd.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter:row.code for index, row in nato_alphabet_df.iterrows()}

user_word = input("Write a word: ").upper()

hidden_word = [nato_alphabet[letter] for letter in user_word]

print(hidden_word)

