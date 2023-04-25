STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle
from scoreboard import Scoreboard

scoreboard=Scoreboard()

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("turtle")
        self.seth(90)
        self.setpos(STARTING_POSITION)
        self.color("white")

    def up(self):
        self.setpos(self.xcor(),self.ycor()+MOVE_DISTANCE)

    def reached_end(self):
        if self.ycor()==FINISH_LINE_Y:
            self.setpos(STARTING_POSITION)
            scoreboard.increase_level()
