from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
COUNTDOWN = 1000 * 3 #in seconds
chosen_word = {}

try:
    data_df = (pd.read_csv("./data/words_to_learn.csv"))
except (FileNotFoundError, pd.errors.EmptyDataError):
    data_df = (pd.read_csv("./data/french_words.csv"))

language = data_df.columns[0]
native_language = data_df.columns[1]
data = data_df.to_dict(orient="records")
chosen_word = {}

def skip_word():
    pass

def clear_word():
    pass

def next_word():
    global chosen_word
    global flip_timer
    window.after_cancel(flip_timer)

    chosen_word = random.choice(data)
    f_word = chosen_word[language]
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.itemconfig(language_label, text=language, fill="black")
    canvas.itemconfig(word, text=f_word, fill="black")
    flip_timer = window.after(COUNTDOWN, func=flip_card)

def flip_card():
    native_word = chosen_word[native_language]
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(language_label, text=native_language, fill="white")
    canvas.itemconfig(word, text=native_word, fill="white")

def remove_word():
    data.remove(chosen_word)
    updated_data = pd.DataFrame(data)
    updated_data.to_csv("data/words_to_learn.csv", index=False)
    next_word()


#Picks a card and word entry without creating a dictionary from the data
#def pick_a_word():
    #pick = data.sample(1)
    #f_word = pick[language].iloc[0]
    #print(pick)
    #print(f_word)

    #en_word = pick["English"].iloc[0]
    #print(en_word)
    #canvas.itemconfig(word, text=f_word)


window = Tk()
window.title("FlashCard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(COUNTDOWN, func=flip_card)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
language_label = canvas.create_text(400, 150, text="", fill="black", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", fill="black", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, command=next_word, highlightthickness=0)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, command=remove_word, highlightthickness=0)
right_button.grid(column=1, row=1)

next_word()


window.mainloop()