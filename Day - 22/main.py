from turtle import Screen
from pong_paddle import Paddle
from ball_class import Ball
from scoreboard import Score
import time
screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=1000, height=800)
screen.tracer(0)
r_paddle = Paddle((450, 0))
l_paddle = Paddle((-450, 0))
ball = Ball()
score = Score()
screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
# Game LOOP
value = True
while value:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce()
    if ball.distance(r_paddle) < 60 and ball.xcor() > 370 or ball.distance(l_paddle) < 60 and ball.xcor() < -370:
        ball.bounce_paddle()
    if ball.xcor() > 450:
        score.l_point()
        ball.reset_ball()
    if ball.xcor() < -450:
        score.r_point()
        ball.reset_ball()
screen.exitonclick()
