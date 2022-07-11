from turtle import Turtle
import config

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = config.BALL_SPEED
        self.dy = config.BALL_SPEED