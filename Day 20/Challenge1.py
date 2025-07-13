from turtle import Screen, Turtle
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
xpos = 0
for _ in range(0,3):
    new_square = Turtle("square")
    new_square.color("white")
    new_square.penup()
    new_square.goto(x=xpos,y=0)
    xpos -= 20



screen.exitonclick()