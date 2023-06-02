from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -280)
        self.left(90)

    def up(self):
        self.forward(8)

    def down(self):
        self.backward(8)

    def reset(self):
        self.goto(0, -280)


