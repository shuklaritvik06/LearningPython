from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=320)
        self.update_score()

    def update_score(self):
        self.write(f"Score = {self.score}", align="center",
                   font=("Arial", 20, "normal"))

    def increasescore(self):
        self.clear()
        self.score += 1
        self.update_score()

    def gameOver(self):
        self.goto(0, 0)
        self.write("Game Over", align="center",
                   font=("Arial", 20, "normal"))
