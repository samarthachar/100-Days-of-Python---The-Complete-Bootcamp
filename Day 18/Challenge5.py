from turtle import Turtle, Screen, colormode
import random
timmy = Turtle()
timmy.shape("turtle")
timmy.speed("fastest")

def random_color():
    colormode(255)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(2)
screen = Screen()
screen.exitonclick()