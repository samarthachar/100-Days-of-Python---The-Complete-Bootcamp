from turtle import Turtle, Screen, colormode
timmy = Turtle()
timmy.shape("turtle")
timmy.pensize(15)
timmy.speed("fastest")

# Types of import
# import turtle
# from turtle import Turtle
# from turtle import * (Imports everything)
# import turtle as t (imports things with a specified name)
# import heroes (have to install, so click on heroes, click on red lightbulb, click on install package
# print(heroes.gen())


import turtle as t
import random
# timmy = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

direction = [90,180,270,360]


for _ in range(250):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(direction))


screen = Screen()
screen.exitonclick()