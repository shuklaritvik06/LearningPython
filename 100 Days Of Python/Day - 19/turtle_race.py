import random
from turtle import Turtle, Screen
screen = Screen()
colors = ["red", "blue", "yellow", "pink", "green", "purple"]
y_pos = [-140, -100, -60, -20, 20, 60]
post = [10, 20, 30, 40]
all_turtles = []
screen.setup(width=600, height=500)
user_input = screen.textinput(title="Make your bet",
                              prompt="Which turtle will win the race?")

for index in range(6):
    myturtle = Turtle(shape="turtle")
    myturtle.penup()
    myturtle.goto(x=-290, y=y_pos[index])
    myturtle.color(colors[index])
    all_turtles.append(myturtle)

if user_input:
    value = True

while value:
    for aturtle in all_turtles:
        position = random.choice(post)
        aturtle.forward(position)
        if aturtle.xcor() > 290:
            value = False
            mycolor = aturtle.pencolor()
            if mycolor == user_input:
                print(f"You've won! The {mycolor} color won the race!")
                screen.done()
            else:
                print(f"You've lost! The {mycolor} color is the winner")
