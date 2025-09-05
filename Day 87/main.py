from turtle import Screen
from paddle import Paddle
from ball import Ball
from game_block import Block
import time

def up_clicked():
    global game_is_on
    game_is_on = True

screen = Screen()
screen.setup(width= 500, height=500)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle = Paddle((0,-200))

ball = Ball(0,-175)

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")
screen.onkey(up_clicked, "Up")
game_is_on = False

while not game_is_on:
    screen.update()
    block = Block()

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

screen.exitonclick()