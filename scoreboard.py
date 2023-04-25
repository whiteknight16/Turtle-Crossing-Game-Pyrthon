from turtle import Turtle
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.color("white")
        self.setpos(-260, 250)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level:{self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.pu()
        self.hideturtle()
        self.color("white")
        self.setpos(0, 0)
        self.write(f"Game Over", align="center", font=FONT)
