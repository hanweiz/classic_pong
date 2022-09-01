from turtle import Turtle, Screen

class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()
        
    
    def l_point(self):
        self.l_score += 1
        self.update_score()
    
    def r_point(self):
        self.r_score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-150, 280)
        self.write(self.l_score, align="center", font=("Courier", 100, "normal"))
        self.goto(150, 280)
        self.write(self.r_score, align="center", font=("Courier", 100, "normal"))
