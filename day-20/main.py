import time
import turtle as t
import random
from snake import Snake

screen = t.Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)


"""
def create_part():
    new_part = t.Turtle(shape="square")
    new_part.color("white")
    new_part.penup()
    return new_part

def set_starting_snake():
    starting_snake = []
    starting_x = 0
    for i in range(3):
        current_part = create_part()
        current_part.teleport(x=starting_x, y=0)
        starting_snake.append(current_part)
        starting_x -= 20
    return starting_snake

snake = set_starting_snake()
"""

snake = Snake()

while True:
    screen.update()
    time.sleep(0.1)

    snake.move()




screen.exitonclick()
