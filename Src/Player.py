from turtle import Turtle
First_Pos = (0, -280)
End_Pos = 280
step = 10


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def move_forward(self):
        self.forward(step)

    def move_backward(self):
        self.backward(step)

    def move_right(self):
        self.right(step)

    def move_left(self):
        self.left(step)

    def finish_game(self):
        if self.ycor() > End_Pos:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(First_Pos)
