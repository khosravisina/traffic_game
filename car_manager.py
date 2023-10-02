from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
    def make_cars(self):
        if random.randint(1,6) == 1:
            car = Turtle('square')
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto(320, random.randint(-250, 250))
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.seth(180)
            car.forward(self.speed)

    def change_speed(self):
        self.speed += MOVE_INCREMENT
