from turtle import Turtle, Screen, position
import time
dist = 20
pos = [(0, 0), (-20, 0), (-40, 0),  (-60, 0)]
up = 90
down = 270
left = 180
right = 0


class Myturtle:
    def __init__(self):
        self.turtles_list = []
        self.add()
        self.head = self.turtles_list[0]

    def add(self):
        for position in pos:
            self.create(position)

    def create(self, position):
        self.myturtle = Turtle(shape="square")
        self.myturtle.color("white")
        self.myturtle.penup()
        self.myturtle.goto(position)
        self.turtles_list.append(self.myturtle)

    def extend(self):
        self.create(self.turtles_list[-1].position())

    def move(self):
        for turt in range(len(self.turtles_list) - 1, 0, -1):
            self.new_x = self.turtles_list[turt - 1].xcor()
            self.new_y = self.turtles_list[turt - 1].ycor()
            self.turtles_list[turt].goto(self.new_x, self.new_y)
        self.head.forward(dist)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)
