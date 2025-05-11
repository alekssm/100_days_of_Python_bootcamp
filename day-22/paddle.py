from turtle import Turtle
X_DISTANCE = 360

class Paddle:
    def __init__(self, player_number):
        self.player_number = player_number
        self.body = self.set_paddle()

    @staticmethod
    def create_segment():
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        return segment

    def set_paddle(self):
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
        return paddle_body



