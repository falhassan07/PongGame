from turtle import Turtle 


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.paddle = Turtle()
        # self.paddle.speed(0)
        self.paddle.penup()
        self.paddle.shape("square")
        self.paddle.shapesize(5, 1)
        self.paddle.color("white")
        self.paddle.goto(position)
    
    def up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(),new_y)

    def down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(),new_y)
