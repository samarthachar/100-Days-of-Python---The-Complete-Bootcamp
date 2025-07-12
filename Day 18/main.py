from turtle import Turtle, Screen, colormode
timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

# Challenge 1
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)


# Types of import
# import turtle
# from turtle import Turtle
# from turtle import * (Imports everything)
# import turtle as t (imports things with a speified name)
# import heroes (have to install, so click on heroes, click on red lightbulb, click on install package
# print(heroes.gen())


# Challenge 2
# import random
# def random_colour():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     return  r,g,b
# colormode(255)
# for i in range(3,11):
#     timmy.color(random_colour())
#     angle = 360 / i
#     for x in range(i):
#         timmy.forward(100)
#         timmy.right(angle)








screen = Screen()
screen.exitonclick()