import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?" ).lower()


screen.exitonclick()