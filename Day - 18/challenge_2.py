from turtle import Turtle, Screen, forward
myturtle = Turtle()
for _ in range(15):
    myturtle.forward(10)
    myturtle.penup()
    myturtle.forward(10)
    myturtle.pendown()
myscreen = Screen()
myscreen.exitonclick()
