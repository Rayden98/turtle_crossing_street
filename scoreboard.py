from turtle import Turtle


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.color("black")

    def print_level(self):
        self.clear()
        self.goto(-150, 270)
        self.write(self.level, align="center", font=("courier", 20, "normal"))
        self.goto(-220, 270)
        self.write("Level", align="center", font=("courier", 20, "normal"))

    def update_level(self):
        self.level += 1
        self.print_level()

