from turtle import Turtle
FONT = ("Courier", 24, "normal")
GAME_OVER = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.hideturtle()
        self.setpos(-250, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", font=FONT)

    def add_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.setpos(-50, 0)
        self.write("Game Over", font=GAME_OVER)