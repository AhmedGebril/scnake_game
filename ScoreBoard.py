from turtle import Turtle
Font=("Courier",24,"normal")
ALIGNMENT="center"

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        with open("data.ex")as file:
            self.highscore = int(file.read())
        self.goto(0, 265)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"score {self.score} high score{self.highscore}", align=ALIGNMENT, font=Font)


    def resetScore(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("data.ex",mode="w")as data:
                data.write(f"{self.highscore}")
        self.score=0
        self.update_score()


    def increase_score(self):
        self.score+=1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align=ALIGNMENT, font=Font)