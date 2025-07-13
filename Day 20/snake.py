from turtle import Turtle
STARTING_POSITIONS = [(0,0),(0,-20),(0,-40)]
MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        self.squares = []
        self.create_snake()
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_square = Turtle("square")
            new_square.color("white")
            new_square.penup()
            new_square.goto(position)
            self.squares.append(new_square)

    def move(self):
        for sq_num in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[sq_num - 1].xcor()
            new_y = self.squares[sq_num - 1].ycor()
            self.squares[sq_num].goto(new_x, new_y)
        self.squares[0].forward(MOVE_DISTANCE)
        self.squares[0].left(90)

