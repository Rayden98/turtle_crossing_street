import random
from turtle import Turtle, Screen
from car_manager import Car
from player import Player
from scoreboard import Level
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

car = Car()
player = Player()
level = Level()

car.create_a_car_line()

level.print_level()
screen.listen()

screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

game_is_on = True
while game_is_on:
    counter = random.randint(2, 100)
    time.sleep(0.1)

    screen.update()

    car.movement_straight()
    if counter % 15 == 0 or (counter > 98) or (counter < 3) or (47 < counter < 50):
        car.create_a_car_line()
    car.eliminate_cars()

    for every_car in car.list_of_cars:
        if player.distance(every_car) < 20:
            game_is_on = False

    if player.ycor() > 280:
        level.update_level()
        player.reset()
        car.level_up()

screen.exitonclick()
