from turtle import Turtle
X_DISTANCE = 360
PADDLE_PACE = 40
BORDER_DISTANCE = 270

class Paddle:
    def __init__(self, player_number):
        self.player_number = player_number
        self.body = self.set_paddle()
        self.upper_head = self.body[-1]
        self.bottom_head = self.body[0]

    @staticmethod
    def create_segment():
        """Creates a signle segment of the body of the paddle - Turtle object, and returns it"""
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.speed("fastest")
        return segment

    def set_paddle(self):
        """Creates the paddle body by setting the coordinates of each paddle segment and returns them in a list"""
        paddle_body = []
        starting_y = -30
        if self.player_number == 1:
            x = -X_DISTANCE
        else:
            x = X_DISTANCE

        for i in range(4):
            current_segment = self.create_segment()
            current_segment.teleport(x=x, y=starting_y)
            paddle_body.append(current_segment)
            starting_y += 20

        paddle_body[-1].setheading(90)
        paddle_body[0].setheading(270)

        return paddle_body

    def move_down(self):
        if self.bottom_head.ycor() > - BORDER_DISTANCE:
            for body_part_num in range(len(self.body) - 1, 0, -1):
                new_y = self.body[body_part_num - 1].ycor() - 20
                x = self.body[0].xcor()
                self.body[body_part_num].goto(x, new_y)
            self.bottom_head.forward(PADDLE_PACE)

    def move_up(self):
        if self.upper_head.ycor() < BORDER_DISTANCE:
            for body_part_num in range(0,len(self.body) - 1):
                x = self.body[0].xcor()
                new_y = self.body[body_part_num + 1].ycor() + 20
                self.body[body_part_num].goto(x, new_y)
            self.upper_head.forward(PADDLE_PACE)



