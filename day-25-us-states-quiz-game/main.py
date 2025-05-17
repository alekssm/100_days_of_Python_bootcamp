import turtle as t
import pandas as pd

screen = t.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)

data = pd.read_csv("50_states.csv")
states = list(data.state)
x_coordinates = list(data.x)
y_coordinates = list(data.y)

writer = t.Turtle()
writer.hideturtle()
writer.penup()

states_data = {}

for i in range(len(states)):
    states_data[states[i]] = x_coordinates[i], y_coordinates[i]

guessed_states = set()

while len(guessed_states) < len(states):
    user_answer = screen.textinput("Guess a state", "Enter a state name:").title()

    if user_answer == "Exit":
        break
    if user_answer in states:
        writer.goto(states_data[user_answer])
        writer.write(f"{user_answer}", align='center', font=('Arial', 13, 'normal'))
        guessed_states.add(user_answer)

not_guessed_states = set(states) - guessed_states
new_data = pd.DataFrame(not_guessed_states)

new_data.to_csv("new_states_to_learn.csv")


t.mainloop()