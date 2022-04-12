from turtle import Turtle, Screen, color, forward
import random


def move(i):
    myturtle.color(random.choice(colors))
    for _ in range(i):
        myturtle.forward(100)
        myturtle.left(360/i)


myturtle = Turtle()
i = 3
colors = ['dark khaki', 'firebrick', 'pink',
          'green', 'blue', 'yellow', 'brown', 'purple']
while i <= 10:
    move(i)
    i += 1
myscreen = Screen()
myscreen.exitonclick()
