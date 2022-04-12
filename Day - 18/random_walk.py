from turtle import Turtle, Screen
import random
myturtle = Turtle()
colors = ['dark khaki', 'firebrick', 'pink',
          'LemonChiffon2', 'HotPink1', 'LightSeaGreen', 'HotPink4']
directions = [0, 90, 180, 270]
myturtle.pensize(15)
for _ in range(500):
    myturtle.forward(40)
    myturtle.setheading(random.choice(directions))
    myturtle.color(random.choice(colors))
myscreen = Screen()
myscreen.exitonclick()
