import turtle
import turtle as t
import random

t.colormode(255)

angles = [0, 90, 180, 270]

def random_color():
    rgb = tuple(random.randint(1,255) for _ in range(3))
    return rgb

timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("DarkOrange")
timmy.speed("fastest")

def draw_spirograph(turtle, circle_size, step):

    for i in range(0, 360, 5):
        turtle.color(random_color())
        turtle.circle(circle_size)
        turtle.left(step)


screen = t.Screen()
screen.exitonclick()