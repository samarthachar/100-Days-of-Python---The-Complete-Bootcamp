from turtle import Turtle

class Ball(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_distance = 10
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.reset_position(xcor,ycor)
    def move(self):
        new_x =  self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
    def reset_position(self, xcor, ycor):
        self.goto(xcor,ycor)
        self.move_speed = 0.1
        self.bounce_x()