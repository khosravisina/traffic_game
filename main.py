import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(key='w', fun=player.move_up)
screen.onkey(key='s', fun=player.move_down)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    cars.make_cars()
    cars.move()
    for car in cars.cars:
        if player.distance(car)<20:
            score.gave_over()
            game_is_on = False

    if player.finish_line():
        cars.change_speed()
        score.updata_level()

screen.exitonclick()

