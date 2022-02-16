import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
carManager = CarManager(600)
froger = Player()

game_is_on = True
screen.listen()

screen.onkeypress(fun=froger.move_up, key="Up")
screen.onkeypress(fun=froger.move_down, key="Down")

while game_is_on:
    time.sleep(0.1)
    carManager.move_cars(froger, scoreboard.score)

    if froger.ycor() > 250:
        scoreboard.add_score()
        froger.reset()

    if carManager.collision:
        game_is_on = False
    screen.update()

scoreboard.game_over()
screen.exitonclick()
