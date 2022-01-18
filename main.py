from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.bgcolor("medium violet red")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle_left = Paddle()
paddle_right = Paddle()

screen.listen()
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")

playing = True
while playing:
    screen.update()

screen.exitonclick()