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



direction = [90,180,270,360]
for _ in range(250):
    timmy.color(random_colour())
    timmy.forward(30)
    timmy.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()