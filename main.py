from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0) #turn off animation
ball_speed = 0.1

right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s") 


game_is_on = True 

while game_is_on:
    time.sleep(ball_speed)
    screen.update()
    ball.move()

    #collision with top and bottom  
    if ball.ycor() > 280 or ball.ycor() < -280: 
        ball.bounce_y() 


    #collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x() 
        ball_speed *= 0.9

    #when ball misses  right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        ball_speed = 0.1

    #when ball misses  left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        ball_speed = 0.1

screen.exitonclick()