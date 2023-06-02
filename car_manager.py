from turtle import Turtle
import random


vertical_random_line = [(295, 260), (295, 220), (295, 180), (295, 140), (295, 100), (295, 60), (295, 10), (295, -30), (295, -70), (295, -110), (295, -150), (295, -190)]
colors = ["red", 'orange', 'yellow', 'green', 'blue', 'purple']


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.forward_movement = 5
        self.list_of_cars = []

    def create_a_car_line(self):
        for position in vertical_random_line:
            number_of_car = random.randint(1, 4)
            if number_of_car == 3:
                new_xcor = random.randint(5, 58)
                self.add_a_car(position, new_xcor)

    def add_a_car(self, position, new_xcor):
        new_car = Turtle("square")
        new_car.color(random.choice(colors))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.left(180)
        new_car.goto((position[0] + new_xcor), position[1])
        print(new_xcor)
        self.list_of_cars.append(new_car)

    def movement(self):
        self.goto(random.choice(vertical_random_line))

    def movement_straight(self):
        self.clear()
        for each in range(len(self.list_of_cars)):
            self.list_of_cars[each].forward(self.forward_movement)

    def eliminate_cars(self):

        for each in self.list_of_cars:
            count = 0
            if each.xcor() < -360:
                each.hideturtle()
                del self.list_of_cars[count]
                #print(self.list_of_cars)
            count += 1

    def level_up(self):
        self.forward_movement += 3
