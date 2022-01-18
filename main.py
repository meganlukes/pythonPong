from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("medium violet red")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle_left = Paddle((-350, 0))
paddle_right = Paddle((350, 0))
ball = Ball()

screen.listen()
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")

playing = True

while playing:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()