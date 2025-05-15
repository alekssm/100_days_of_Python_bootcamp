from turtle import Turtle

with open("data.txt") as file:
    highscore = int(file.read())

ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = highscore
        self.hideturtle()
        self.penup()
        self.teleport(0, 270)
        self.color("white")
        self.score_writer()

    def score_counter(self):
        self.score += 1
        self.score_writer()

    def score_writer(self):
        self.write(arg=f"Score: {self.score} Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def set_new_highscore(self):
        if self.score > self.highscore:
            with open("data.txt", "w") as data:
                data.write(str(self.score))


    def game_over(self):
        self.set_new_highscore()
        self.teleport(0, 0)
        self.write(arg="Game over", align=ALIGNMENT, font=FONT)
