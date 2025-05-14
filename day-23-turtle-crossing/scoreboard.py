from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.player_level = 0
        self.hideturtle()
        self.penup()
        self.color("black")
        self.teleport(x=-280, y=260)
        self.level_writer()

    def level_counter(self):
        self.player_level += 1
        self.clear()
        self.level_writer()

    def level_writer(self):
        self.write(arg=f"Level: {self.player_level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game over", align="center", font=FONT)

