from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.cars_move_speed = -STARTING_MOVE_DISTANCE

    def create_car(self):
        i = random.randint(1, 10)
        if i == 10:
            new_car = Car()
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.cars_move_speed)

    def level_up(self):
        self.cars_move_speed -=MOVE_INCREMENT


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(x=300, y=random.randint(-240, 240))

