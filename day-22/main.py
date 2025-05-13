import time
import turtle as t
import random
from ball import Ball
from scoreboard import Scoreboard, draw_a_white_line
from new_paddle import Paddle


screen = t.Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("My pong game")
screen.tracer(0)
screen.listen()

draw_a_white_line()

player1 = Paddle(1)
player2 = Paddle(2)
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(player2.move_up, "Up")
screen.onkey(player2.move_down, "Down")
screen.onkey(player1.move_up, "w")
screen.onkey(player1.move_down, "s")

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #Checks if the ball has collided with top and bot wall and if so bounces from it
    if ball.detect_collision_with_wall():
        ball.bounce_from_wall()


    #Checks if the ball has collided with any of the paddles and if so bounces from it
    if ball.distance(player1) < 50 and ball.xcor() < -330 or ball.distance(player2) < 50 and ball.xcor() > 330:
        ball.bounce_from_paddle()

    #Checks if the ball is outside the gaming screen and if so scores a point depending on the side
    # on which it left also resets the ball in the center
    if ball.xcor() > 360:
        scoreboard.score_counter(1)
        ball.reset_position()
    elif ball.xcor() < -360:
        scoreboard.score_counter(2)
        ball.reset_position()


screen.exitonclick()
