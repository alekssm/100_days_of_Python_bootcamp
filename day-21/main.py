import time
import turtle as t
import random
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = t.Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
screen.listen()


snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_left, "Left")


game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


    #Detects collision with the wall and ends the game cycle if so
    if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
        scoreboard.game_over()
        game_on = False

    #Detexts collision with the tail of the snake and ends the game cycle if so
    for part in snake.body[1:]:
        if snake.head.distance(part) < 15:
            scoreboard.game_over()
            game_on = False

    #Detects collision with the food and updates the scoreboard
    if snake.head.distance(food) < 15:
        scoreboard.clear()
        scoreboard.score_counter()
        snake.extend()
        food.set_position()




screen.exitonclick()