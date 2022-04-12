from turtle import Turtle, Screen, forward
i_am_like_him = Turtle()
i_am_like_him.shape('turtle')
i_am_like_him.color('blue')
myscreen = Screen()
for _ in range(4):
    i_am_like_him.forward(100)
    i_am_like_him.right(90)
myscreen.exitonclick()
