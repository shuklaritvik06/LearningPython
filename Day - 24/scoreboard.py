from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.highscore = 0
        self.update_score()

    def update_score(self):
        self.goto(x=-50, y=320)
        self.write(f"Score = {self.score}", align="center",
                   font=("Arial", 10, "normal"))
        self.goto(x=+100, y=320)
        with open("highscore.txt", "r+") as file:
            myscore = file.read()
        self.highscore = int(myscore)
        self.write(f"High Score = {self.highscore}", align="center",
                   font=("Arial", 10, "normal"))

    def increasescore(self):
        self.clear()
        self.score += 1
        self.update_score()

    def calchighscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
        with open("highscore.txt", "w") as file:
            file.write(f"{self.highscore}")
        self.clear()
        self.update_score()

    def gameOver(self):
        self.goto(0, 0)
        self.write("Game Over", align="center",
                   font=("Arial", 20, "normal"))
