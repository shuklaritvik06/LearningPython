import random
import turtle as t
myturtle = t.Turtle()
directions = [0, 90, 180, 270]

t.colormode(255)
myturtle.pensize(18)
myturtle.speed("fast")


def randomcol():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    randomcolor = (r, g, b)
    return randomcolor


for _ in range(500):
    myturtle.forward(50)
    myturtle.right(random.choice(directions))
    myturtle.color(randomcol())

myscreen = t.Screen()
myscreen.exitonclick()
