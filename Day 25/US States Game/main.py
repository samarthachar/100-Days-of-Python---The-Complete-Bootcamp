import turtle, pandas
from turtle import Turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.screensize(491,725)
turtle.shape(image)

score = 0
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?" )
    if answer_state in all_states:
        score += 1
        turtle = Turtle()
        turtle.penup()
        state_data = data[data.state == answer_state]
        turtle.goto(state_data.x.item,state_data.y.item)
        turtle.write(state_data.state)

screen.exitonclick()