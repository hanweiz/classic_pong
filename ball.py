from turtle import Turtle
import config

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = config.BALL_DX
        self.dy = config.BALL_DY
    
    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)
    
    def bounce(self):
        self.dy *= -1