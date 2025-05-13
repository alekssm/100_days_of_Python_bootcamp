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
        self.clear()
        self.score_writer()

    def score_writer(self):
        self.write(arg=f"{self.player1_score}    {self.player2_score}", align=ALIGNMENT, font=FONT)


def draw_a_white_line():
    """Draws the white line that splits the gaming field"""
    white_line = Turtle()

    white_line.teleport(x=0, y=300)
    white_line.color("white")
    white_line.hideturtle()
    white_line.speed("fastest")
    white_line.pensize(4)
    white_line.setheading(270)
    for i in range(0, 600, 20):
        white_line.forward(20)
        white_line.penup()
        white_line.forward(20)
        white_line.pendown()
