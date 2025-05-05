import turtle as t
import random
t.colormode(255)

colors = ["red", "blue", "green", "yellow", "purple"]

timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("DarkOrange")

def draw_square(turtle, distance):
    for _ in range(4):
        turtle.fd(distance)
        turtle.lt(90)

def draw_dashed_line(turtle, line_size, distance):
    current_distance = 0
    while current_distance < distance:
        turtle.forward(line_size)
        turtle.penup()
        turtle.forward(line_size)
        timmy.pendown()

def draw_shape(turtle, sides, side_size):
    angle = 180 - ((sides - 2) * 180 / sides)
    for _ in range(sides):
        turtle.fd(side_size)
        turtle.rt(angle)

def random_color():
    rgb = tuple(random.randint(1,255) for _ in range(3))
    return rgb

def draw_spirograph(turtle, circle_size, step):

    for i in range(0, 360, 5):
        turtle.color(random_color())
        turtle.circle(circle_size)
        turtle.left(step)


screen = t.Screen()
screen.exitonclick()

