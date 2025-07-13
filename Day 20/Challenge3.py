from turtle import Screen, Turtle
import time


screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

xpos = 0


squares = []

for _ in range(0,3):
    new_square = Turtle("square")
    new_square.color("white")
    new_square.penup()
    new_square.goto(x=xpos,y=0)
    squares.append(new_square)
    xpos -= 20



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for sq_num in range(len(squares)-1,0,-1):
        new_x = squares[sq_num - 1].xcor()
        new_y = squares[sq_num - 1].ycor()
        squares[sq_num].goto(new_x,new_y)
    squares[0].forward(20)
    squares[0].left(90)
screen.exitonclick()