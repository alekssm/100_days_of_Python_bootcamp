from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Roboto', 41, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player1_score = 0
        self.player2_score = 0
        self.hideturtle()
        self.penup()
        self.teleport(0, 240)
        self.color("white")
        self.score_writer()

    def score_counter(self, player):
        if player == 1:
            self.player1_score += 1
        elif player == 2:
            self.player2_score += 1

    def score_writer(self):
        self.write(arg=f"{self.player1_score}    {self.player2_score}", align=ALIGNMENT, font=FONT)


