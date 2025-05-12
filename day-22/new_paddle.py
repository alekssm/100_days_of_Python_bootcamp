from turtle import Turtle
X_DISTANCE = 360
BORDER_DISTANCE = 240
PADDLE_PACE = 20

class Paddle(Turtle):
    def __init__(self, player_number):
        super().__init__()
        self.player_number = player_number
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.set_paddle()

    def set_paddle(self):
        if self.player_number == 1:
            self.teleport(x= -X_DISTANCE, y=0)
        else:
            self.teleport(x=X_DISTANCE, y=0)

    def move_down(self):
        if self.ycor() > -BORDER_DISTANCE:
            new_y = self.ycor() - PADDLE_PACE
            self.goto(x=self.xcor(), y=new_y)

    def move_up(self):
        if self.ycor() < BORDER_DISTANCE:
            new_y = self.ycor() + PADDLE_PACE
            self.goto(x=self.xcor(), y=new_y)
