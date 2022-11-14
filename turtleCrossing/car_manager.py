import random
from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
ENDING_POINT_X = -350


class CarManager():
#Create a car list and set a movement speed
    def __init__(self):
        self.allCars = []
        self.carSpeed = STARTING_MOVE_DISTANCE

#Create randomly generated cars
    def createCars(self):
        randomChance = random.randint(1,6)
        if randomChance == 1:
            newCar = Turtle('square')
            newCar.color(choice(COLORS))
            newCar.penup()
            randomY = random.randint(-250,250)
            newCar.goto(300,randomY)
            newCar.shapesize(stretch_wid=1, stretch_len=2)
            self.allCars.append(newCar)

    #Make the cars move
    def moveCars(self):
        for car in self.allCars:
            car.backward(self.carSpeed)

    #Speed up the cars
    def speedUp(self):
        self.carSpeed += MOVE_INCREMENT

