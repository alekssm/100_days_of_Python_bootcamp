import turtle as t
import random

colors = ["red", "blue", "green", "yellow", "purple"]
angles = [0, 90, 180, 270]

timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("DarkOrange")
timmy.pen(pensize=5)
timmy.speed("fast")


def random_walk(turtle, step_size):
    turtle.rt(random.choice(angles))
    turtle.forward(step_size)

for i in range(random.randint(0, 100)):
    timmy.color(random.choice(colors))
    random_walk(timmy, 20)




screen = t.Screen()
screen.exitonclick()