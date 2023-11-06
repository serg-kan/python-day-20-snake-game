from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.color("white")

        self.score = 0

    def update_score(self):
        self.score += 1

    def print_score(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 16, "normal"))

    def print_game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", move=False, align="center", font=("Arial", 24, "normal"))