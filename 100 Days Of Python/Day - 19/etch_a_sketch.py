from turtle import Turtle, Screen
myturtle = Turtle()


def movefd():
    myturtle.forward(20)


def movebd():
    myturtle.backward(20)


def anticlock():
    myturtle.left(5)


def clock():
    myturtle.right(5)


# def clear():
#     myturtle.reset()


def clear():
    myturtle.clear()
    myturtle.penup()
    myturtle.home()
    myturtle.pendown()


screen = Screen()
screen.listen()
screen.onkey(key="w", fun=movefd)
screen.onkey(key="s", fun=movebd)
screen.onkey(key="a", fun=anticlock)
screen.onkey(key="d", fun=clock)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
