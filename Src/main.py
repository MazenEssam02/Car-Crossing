from Player import Player
from Car import Car
from Score import Score
from turtle import Turtle, Screen
import time

def game_boundaries():
    turtle = Turtle()
    turtle.color("white")
    turtle.hideturtle()
    turtle.pu()
    turtle.goto(-300, -300)
    turtle.pd()
    turtle.speed('fastest')
    for i in range(4):
        turtle.forward(600)
        turtle.left(90)
    
def start_game():
    flag=1
    while flag:
        
        time.sleep(t)
        screen.update()
        cars.new_car()
        cars.move_cars()
    
    
        for car in cars.all_cars:
            if car.distance(player) < 20:
                flag = 0
                score.game_over()
                
        if player.finish_game():
            player.go_to_start()
            score.level_up()
            cars.car_speed_up()
            cars.increament_cars()
t = 0.1
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)
game_boundaries()
screen.tracer(0)
player = Player()
score = Score()
cars = Car()
screen.listen()
screen.onkeypress(player.move_forward, 'Up')
screen.onkeypress(player.move_backward, 'Down')
start_game()   
screen.exitonclick()
