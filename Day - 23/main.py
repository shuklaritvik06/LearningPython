import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Race")
screen.setup(width=600, height=600)
screen.tracer(0)
myplayer = Player()
cars = CarManager()
score = Scoreboard()
screen.listen()
screen.onkey(myplayer.move, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    cars.create()
    cars.move()
    for car in cars.mycars:
        if myplayer.distance(car) < 20:
            score.game_over()
            game_is_on = False

    if myplayer.ycor() > 280:
        score.increase_level()
        myplayer.reset_game()
        cars.move_increment()
    screen.update()
screen.exitonclick()
