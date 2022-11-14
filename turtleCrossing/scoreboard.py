from turtle import Turtle
FONT = ("Courier", 24, "normal")
X = -250
Y = 250

#Create the Scoreboard
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(X, Y)
        self.level = 1
        self.write(f"Level: {self.level}", True, align = "left", font = FONT)

#Update the scoreboard
    def levelUp(self):
        self.clear()
        self.goto(X,Y)
        self.level += 1
        self.write(f"Level: {self.level}", True, align="left", font=FONT)

#GameOver
    def gameOver(self):
        self.clear()
        self.goto(-100,0)
        self.write("Game Over", font=FONT)

