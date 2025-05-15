import turtle as t

SNAKE_PACE = 20


class Snake:

    def __init__(self):
        self.body = self.set_starting_snake()
        self.head = self.body[0]

    def create_part(self, x_position, y_position):
        """Creates a part of the snake as Turtle object and returns it"""
        new_part = t.Turtle(shape="square")
        new_part.color("white")
        new_part.penup()
        new_part.teleport(x_position, y_position)
        return new_part

    def set_starting_snake(self):
        """Creates and sets the starting position of the snake from 3 Turtle objects"""
        starting_snake = []
        starting_x = 0
        for i in range(3):
            current_part = self.create_part(x_position=starting_x, y_position=0)
            starting_snake.append(current_part)
            starting_x -= 20
        return starting_snake

    def extend(self):
        """Creates a new part of the snake and adds it at the last position of the body"""
        last_part_x = self.head.xcor()
        last_part_y = self.head.ycor()
        self.body.append(self.create_part(last_part_x, last_part_y))


    def move(self):
        for body_part_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[body_part_num - 1].xcor()
            new_y = self.body[body_part_num - 1].ycor()
            self.body[body_part_num].goto(new_x, new_y)
        self.head.forward(SNAKE_PACE)

    def move_up(self):
        if self.head.heading() != 270 and self.head.heading() !=90:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != 90 and self.head.heading() != 270:
            self.head.setheading(270)

    def move_right(self):
        if self.head.heading() != 180 and self.head.heading() != 360:
            self.head.setheading(360)

    def move_left(self):
        if self.head.heading() != 360 and self.head.heading() != 180:
            self.head.setheading(180)