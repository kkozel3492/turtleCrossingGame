from turtle import Turtle

import scoreboard
from scoreboard import Scoreboard

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 280


# Create the turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    # Move the turtle
    def moveUp(self):
        newPosition = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), newPosition)

    def moveLeft(self):
        newPosition = self.xcor() - MOVE_DISTANCE
        self.goto(newPosition, self.ycor())

    def moveRight(self):
        newPosition = self.xcor() + MOVE_DISTANCE
        self.goto(newPosition, self.ycor())

    #Did he cross the finish
    def crossFinish(self, score):
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            score.levelUp()
            return True
        else:
            return False




