from turtle import Turtle, Screen
myturtle = Turtle()
myturtle.speed("fast")


def move():
    myturtle.forward(20)


screen = Screen()
screen.listen()
screen.onkeypress(key="space", fun=move)
screen.exitonclick()
