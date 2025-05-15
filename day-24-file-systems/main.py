#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()

with open("./Input/Letters/starting_letter.txt") as blank_letter:
    letter = blank_letter.read()

for name in names:
    with open(f"./Output/ReadyToSend/{name.strip()}_letter.txt", mode="w") as new_letter:
        letter_text_replaced = letter.replace('[name]', name.strip())
        new_letter.write(f"{letter_text_replaced}")