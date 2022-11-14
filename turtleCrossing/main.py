import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
level = Scoreboard()
person = Player()
cars = CarManager()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.createCars()
    cars.moveCars()
    screen.listen()
    screen.onkey(person.moveUp, 'Up')
    screen.onkey(person.moveLeft, 'Left')
    screen.onkey(person.moveRight, 'Right')


    if person.crossFinish(level):
        cars.speedUp()


    for car in cars.allCars:
        if car.distance(person) < 20:
            level.gameOver()
            game_is_on = False

screen.exitonclick()





