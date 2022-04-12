from turtle import Turtle, color, Screen, end_fill
myturtle = Turtle()
myscreen = Screen()
myscreen.title("Learning Turtle Graphic")
myturtle.color('red', 'yellow')
myturtle.begin_fill()
for _ in range(4):
    myturtle.forward(200)
    myturtle.left(90)
myturtle.end_fill()
myscreen.exitonclick()
