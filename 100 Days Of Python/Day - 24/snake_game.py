from snake_game_class import Myturtle
from snake_food import Food
from turtle import Screen
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=800, height=700)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snakeg = Myturtle()
screen.listen()
food = Food()
score = Scoreboard()
screen.onkey(snakeg.up, "Up")
screen.onkey(snakeg.down, "Down")
screen.onkey(snakeg.left, "Left")
screen.onkey(snakeg.right, "Right")
value = True
while value:
    screen.update()
    time.sleep(0.1)
    snakeg.move()

    if snakeg.head.distance(food) < 20:
        score.increasescore()
        snakeg.extend()
        food.refresh()

    if snakeg.head.xcor() > 390 or snakeg.head.xcor() < -390 or snakeg.head.ycor() > 340 or snakeg.head.ycor() < -340:
        score.calchighscore()
        score.gameOver()
        value = False

    for element in snakeg.turtles_list[1:]:
        if snakeg.head.distance(element) < 10:
            score.gameOver()
            value = False

screen.exitonclick()
