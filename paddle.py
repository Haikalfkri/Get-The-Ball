from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()
        self.goto(0, -260)
        
    
    def right_move(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())
        
    def left_move(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())