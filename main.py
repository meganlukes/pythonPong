from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("medium violet red")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle_left = Paddle((-350, 0))
paddle_right = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")

playing = True
left_score = 0
right_score = 0
while playing:
    time.sleep(0.1)
    screen.update()
    ball.move()
    scoreboard.update_scoreboard(left_score, right_score)
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce()
    if ball.xcor() > 330 and ball.distance(paddle_right) < 60:
        ball.hit()
    if ball.xcor() < -330 and ball.distance(paddle_left) < 60:
        ball.hit()
    if ball.xcor() > 420 and ball.distance(paddle_right) > 60:
        ball.miss()
        ball.hit()
        left_score += 1

    if ball.xcor() < -420 and ball.distance(paddle_left) > 60:
        ball.miss()
        ball.hit()
        right_score += 1

    if right_score == 2 or left_score == 2:
        scoreboard.update_scoreboard(left_score, right_score)
        scoreboard.game_over(left_score, right_score)
        playing = False

screen.exitonclick()