from turtle import Turtle, Screen, colormode
timmy = Turtle()
timmy.shape("turtle")
timmy.pensize(15)
timmy.speed("fastest")

import random
def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return  r,g,b
colormode(255)
for i in range(3,11):
    timmy.color(random_colour())
    angle = 360 / i
    for x in range(i):
        timmy.forward(100)
        timmy.right(angle)

screen = Screen()
screen.exitonclick()