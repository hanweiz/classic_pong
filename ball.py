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
        self.move_speed = 0.05
    
    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1
        self.move_speed *= 0.9
    
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.05
        self.bounce_x()