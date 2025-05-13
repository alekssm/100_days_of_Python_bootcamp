from turtle import Turtle
BALL_PACE = 10

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = BALL_PACE
        self.y_move = BALL_PACE
        self.move_speed = 0.1

    def detect_collision_with_wall(self):
        if self.ycor() >= 290 or self.ycor() <= -290:
            return True
        else:
            return False

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x,new_y)

    def bounce_from_wall(self):
        self.y_move *= -1

    def bounce_from_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_from_paddle()
        self.move_speed = 0.1
