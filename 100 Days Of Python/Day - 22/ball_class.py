from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1

    def move(self):
        ball_x = self.xcor() + self.xmove
        ball_y = self.ycor() + self.ymove
        self.goto(ball_x, ball_y)

    def bounce(self):
        self.ymove *= -1

    def bounce_paddle(self):
        self.xmove *= -1
        self.move_speed *= 1

    def reset_ball(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_paddle()
