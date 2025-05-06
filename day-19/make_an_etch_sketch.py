import turtle as t


timmy = t.Turtle()
timmy.shape("turtle")


def move_upwards():
    timmy.forward(10)

def move_downwards():
    timmy.backward(10)

def move_right():
    timmy.setheading(timmy.heading() - 10)

def move_left():
    timmy.setheading(timmy.heading() + 10)

def reset():
    timmy.home()
    timmy.clear()

screen = t.Screen()
screen.listen()
screen.onkey(key="w",fun=move_upwards)
screen.onkey(key="s",fun=move_downwards)
screen.onkey(key="d",fun=move_right)
screen.onkey(key="a",fun=move_left)
screen.onkey(key="c", fun=reset)
screen.exitonclick()