from turtle import Turtle

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.score = 0
    self.pu()
    self.goto(0, 170)
    self.color("white")
    self.update_scoreboard()
    self.hideturtle()
    

  def update_scoreboard(self):
    self.write(f"Current Score: {self.score} ", align="center",font=("Arial", 10, "normal"))


  def game_over(self):
    self.setpos(0, 0)
    self.write(f"GAME OVER!", align="center",font=("Arial", 10, "normal"))


  def increase_score(self):
    self.score += 1
    self.clear()
    self.update_scoreboard()
