import random
from extractcolors import rgb_colors
import turtle as t
myturtle = t.Turtle()
myturtle.hideturtle()
t.colormode(255)
myturtle.setheading(225)
myturtle.penup()
myturtle.forward(250)
myturtle.setheading(0)
myturtle.pendown()
myturtle.speed("fast")
for i in range(1, 101):
    myturtle.dot(20, random.choice(rgb_colors))
    myturtle.penup()
    myturtle.forward(50)
    myturtle.pendown()
    if i % 10 == 0:
        myturtle.penup()
        myturtle.setheading(90)
        myturtle.forward(50)
        myturtle.setheading(180)
        myturtle.forward(500)
        myturtle.setheading(0)
        myturtle.pendown()
myscreen = t.Screen()
myscreen.exitonclick()
