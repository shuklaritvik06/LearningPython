import random
import turtle as t
myturtle = t.Turtle()

t.colormode(255)


def randomcol():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    randomcolor = (r, g, b)
    return randomcolor


myturtle.speed("fastest")
for _ in range(75):
    myturtle.color(randomcol())
    myturtle.circle(100)
    myturtle.left(5)
myscreen = t.Screen()
myscreen.exitonclick()
