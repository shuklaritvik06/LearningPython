from turtle import Turtle


FONT = ("Courier", 15, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.Level = 0
        self.hideturtle()
        self.penup()
        self.update_level()

    def update_level(self):
        self.goto(-200, 250)
        self.clear()
        self.write(f"Level: {self.Level}", align="center", font=FONT)

    def increase_level(self):
        self.Level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
