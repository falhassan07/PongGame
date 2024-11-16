from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0) #turn off animation

right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
ball = Ball()


screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s") 


game_is_on = True 

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()












screen.exitonclick()