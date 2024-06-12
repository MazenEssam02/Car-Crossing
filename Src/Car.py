from turtle import Turtle
import random
starting_x_pos = 280
color_list = ["red", "blue", "green", "yellow", "orange"]
starting_move_speed = 5
move_increament = 5
x = 7


class Car():
    def __init__(self):
        self.c = x
        self.all_cars = []
        self.car_speed = starting_move_speed

    def new_car(self):
        car_num = random.randint(1, self.c)
        if car_num == 1:
            car = Turtle('square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(color_list))
            car.penup()
            y_random = random.randint(-250, 250)
            car.goto(starting_x_pos, y_random)
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            if car.xcor()<-279:
                car.hideturtle()

    def car_speed_up(self):
        self.car_speed += move_increament

    def increament_cars(self):
        self.c -= 1
        if self.c <= 2:
            self.c = 2
