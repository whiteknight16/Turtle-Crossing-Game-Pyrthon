COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from random import choice,randint
from turtle import Turtle

class CarManager():
    def __init__(self):
        self.car_list=[]
        self.car_speed=0.1
    
    def create_car(self):
        is_car_crating=randint(1,6)
        if is_car_crating==6:
            t=Turtle()
            t.shape("square")
            t.pu()
            t.setpos(280,randint(-250,250))
            t.shapesize(1,2,1)
            t.color(choice(COLORS))
            self.car_list.append(t)

    def move_car(self):
        for car in self.car_list:
            car.bk(STARTING_MOVE_DISTANCE)

    def increase_car_speed(self):
        self.car_speed*=.1