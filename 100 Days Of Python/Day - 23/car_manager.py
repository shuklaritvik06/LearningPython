from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 20


class CarManager():
    def __init__(self):
        self.mycars = []

    def create(self):
        if random.randint(1, 6) == 1:

            self.myturtle = Turtle(shape="square")
            self.myturtle.shapesize(stretch_wid=1, stretch_len=2)
            self.myturtle.color(random.choice(COLORS))
            self.myturtle.penup()
            self.myturtle.goto(400, random.randint(-250, 250))
            self.mycars.append(self.myturtle)

    def move(self):
        for cars in self.mycars:
            cars.backward(STARTING_MOVE_DISTANCE)

    def move_increment(self):
        for cars in self.mycars:
            new_speed = STARTING_MOVE_DISTANCE+MOVE_INCREMENT
            cars.backward(new_speed)
