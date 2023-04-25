# import required modules and classes
from turtle import Turtle,Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# setting up screen
screen=Screen()
screen.setup(600,600)
screen.tracer(0)
screen.title("Cross the road")
screen.bgcolor("black")
screen.listen()

# Setting up class objects
player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()



screen.onkey(player.up,"Up")







# game function
game_is_on=True
while(game_is_on):
    screen.update()
    time.sleep(car_manager.car_speed)
    car_manager.create_car()
    car_manager.move_car()

    # Check if crossed
    player.reached_end()
    # Detect collision
    for car in car_manager.car_list:
        if car.distance(player)<25:
           scoreboard.game_over()
           game_is_on=False


screen.exitonclick()