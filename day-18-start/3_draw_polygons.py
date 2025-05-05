import turtle as t
import random

colors = ["red", "blue", "green", "yellow", "purple"]

timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("DarkOrange")


def draw_shape(turtle, sides, side_size):
    angle = 180 - ((sides - 2) * 180 / sides)
    for _ in range(sides):
        turtle.fd(side_size)
        turtle.rt(angle)

for i in range(3, 11):
    timmy.color(random.choice(colors))
    draw_shape(timmy, i, 50)


screen = t.Screen()
screen.exitonclick()






