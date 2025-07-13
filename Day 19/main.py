from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

screen.listen()
screen.onkey(key = "space", fun=move_forward)# This is an example of a Higher Order Function(The method{function} onkey is calling the function move_forward).



screen.exitonclick()