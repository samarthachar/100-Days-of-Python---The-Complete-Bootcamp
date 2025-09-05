from turtle import Turtle

class Block(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_wid=2, stretch_len=1)