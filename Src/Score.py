from turtle import Turtle
import random

FONT = ("Courier", 20, "normal")

mot=Turtle()
class Score(Turtle):
    def __init__(self):
        super(Score, self).__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-295, 305)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.color("white")
        self.write(f"Level : {self.level} ", align='left', font=FONT)

        

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align='center', font=FONT)
