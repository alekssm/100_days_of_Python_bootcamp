import random
import turtle as t

t.colormode(255)

color_list = [(51, 42, 32), (102, 86, 70), (181, 157, 113), (90, 97, 88), (91, 53, 42), (71, 67, 49), (38, 44, 35), (146, 131, 98), (49, 40, 43), (224, 205, 135)]

timmy = t.Turtle()
timmy.shape("turtle")
timmy.teleport(-260, -250)
timmy.penup()
timmy.ht()

x = 10
y = 10

for i in range (y):
    for _ in range(x):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(50)
        timmy.dot(20, random.choice(color_list))

    if i < y-1:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(-180)
        timmy.forward(500)
        timmy.setheading(360)

screen = t.Screen()
screen.screensize(100,100)
screen.exitonclick()