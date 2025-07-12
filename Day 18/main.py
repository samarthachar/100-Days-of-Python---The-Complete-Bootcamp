from turtle import Turtle, Screen
timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

# Challenge 1
for i in range(4):
    timmy.forward(100)
    timmy.right(90)


# Types of import
# import turtle
# from turtle import Turtle
# from turtle import * (Imports everything)
# import turtle as t (imports things with a speified name)
# import heroes (have to install, so click on heroes, click on red lightbulb, click on install package
# print(heroes.gen())








screen = Screen()
screen.exitonclick()