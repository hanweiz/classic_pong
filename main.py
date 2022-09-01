from turtle import Turtle, Screen
from paddle import Paddle
import config
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=config.SCREEN_WIDTH, height=config.SCREEN_HEIGHT)
screen.title("All out Pong")
screen.tracer(0)

right_paddle = Paddle(position=(config.SCREEN_WIDTH//2 - 30, 0))
left_paddle = Paddle(position=(-(config.SCREEN_WIDTH//2 - 30), 0)) 
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # logic of what happens when ball approaches the top or bottom edge
    if ball.ycor() > ((config.SCREEN_HEIGHT // 2) - 20) or ball.ycor() < -((config.SCREEN_HEIGHT // 2) - 20):
        ball.bounce_y()
    
    # Detect collision between r_paddle and ball
    if (ball.distance(right_paddle) < 50 and ball.xcor() > ((config.SCREEN_WIDTH // 2) - 60)) or \
        (ball.distance(left_paddle) < 50 and ball.xcor() < -((config.SCREEN_WIDTH // 2) - 60)):
        ball.bounce_x()
    
    # Detect r_paddle miss
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()

    # Detect l_paddle miss
    elif ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()