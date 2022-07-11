from turtle import Turtle, Screen
from paddle import Paddle
import config

screen = Screen()
screen.bgcolor("black")
screen.setup(width=config.SCREEN_WIDTH, height=config.SCREEN_HEIGHT)
screen.title("All out Pong")
screen.tracer(0)

right_paddle = Paddle(position=(config.SCREEN_WIDTH//2 - 30, 0))
left_paddle = Paddle(position=(-(config.SCREEN_WIDTH//2 - 30), 0)) 

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

is_game_on = True
while is_game_on:
    screen.update()


screen.exitonclick()