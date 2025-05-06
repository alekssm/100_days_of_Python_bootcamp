import random
import turtle as t

colors = {"red", "yellow", "green", "blue", "orange", "purple"}
turtles = []

def create_turtle():
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.speed(random.randint(3, 6))
    new_turtle.color(colors.pop())
    return new_turtle

def turtle_set():
    current_y = -75
    for current_turtle in turtles:
        current_turtle.goto(x=-230, y=current_y)
        current_y += 30



for _ in range(6):
    turtles.append(create_turtle())


screen = t.Screen()
screen.listen()
screen.setup(width=500, height=400)
users_bet = screen.textinput(title="Make your bet", prompt="Who will win the race? Enter a color:")

turtle_set()

winner = None
while not winner:
    for current_turtle in turtles:
        current_turtle.forward(random.randint(3, 7))
        if current_turtle.xcor() > 230:
            winner = current_turtle.color()[0]
            if users_bet == winner:
                print(f"Congrats, you won! {winner} is first!")
            else:
                print(f"Sorry, you lose! {winner} is first!")
            break


screen.exitonclick()

