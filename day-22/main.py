import time
import turtle as t
import random
from scoreboard import Scoreboard
from paddle import Paddle

white_line = t.Turtle()

screen = t.Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("My pong game")
screen.tracer(0)
screen.listen()

white_line.teleport(x=0, y=300)
white_line.color("white")
white_line.hideturtle()
white_line.speed("fastest")
white_line.pensize(4)
white_line.setheading(270)
for i in range(0,600, 20):
    white_line.forward(20)
    white_line.penup()
    white_line.forward(20)
    white_line.pendown()

player1 = Paddle(1)
player2 = Paddle(2)

scoreboard = Scoreboard()





game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    screen.onkey(player2.move_up, "Up")
    screen.onkey(player2.move_down, "Down")
    screen.onkey(player1.move_up, "w")
    screen.onkey(player1.move_down, "s")



screen.exitonclick()
