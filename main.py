from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0) #turn off animation

paddle_right = Paddle()


screen.listen()
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")


game_is_on = True 

while game_is_on:
    screen.update()












screen.exitonclick()