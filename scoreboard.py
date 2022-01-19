from turtle import Screen, Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(0, 260)


    def update_scoreboard(self, score1, score2):
        self.clear()
        self.write(f"{score1} : {score2}", align="center", font=("Arial", 20, "normal"))

    def game_over(self, score1, score2):
        self.goto(0, 0)
        winner = "blank"
        if score1 > score2:
            winner = "Player 1"
        else:
            winner = "Player 2"
        self.write(f"{winner} Won!", align="center", font=("Arial", 24, "normal"))