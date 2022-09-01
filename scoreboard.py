from turtle import Turtle, Screen

class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.write(self.l_score, align="center", font=("courier", 48, "normal"))