from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.teleport(0, 270)
        self.color("white")
        self.score_writer()

    def score_counter(self):
        self.score += 1
        self.score_writer()

    def score_writer(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.teleport(0, 0)
        self.write(arg="Game over", align=ALIGNMENT, font=FONT)
