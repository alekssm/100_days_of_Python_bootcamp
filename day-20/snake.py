import turtle as t

def create_part():
    """Creates a part of the snake as Turtle object and returns it"""
    new_part = t.Turtle(shape="square")
    new_part.color("white")
    new_part.penup()
    return new_part

def set_starting_snake():
    """Creates and sets the starting position of the snake from 3 Turtle objects"""
    starting_snake = []
    starting_x = 0
    for i in range(3):
        current_part = create_part()
        current_part.teleport(x=starting_x, y=0)
        starting_snake.append(current_part)
        starting_x -= 20
    return starting_snake


class Snake:
    def __init__(self):
        self.body = set_starting_snake()

    def move(self):
        for body_part_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[body_part_num - 1].xcor()
            new_y = self.body[body_part_num - 1].ycor()
            self.body[body_part_num].goto(new_x, new_y)
        self.body[0].forward(20)


