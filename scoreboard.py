from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.color("white")

        self.score = 0

        with open("highscore.txt") as file:
            high_score = int(file.read())

        self.high_score = high_score

        self.print_score()

    def update_score(self):
        self.score += 1

    def print_score(self):
        self.clear()
        self.write(f"Score: {self.score}, High score: {self.high_score}", move=False, align="center", font=("Arial", 16, "normal"))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score

            with open("highscore.txt", mode="w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.print_score()

    def print_game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", move=False, align="center", font=("Arial", 24, "normal"))