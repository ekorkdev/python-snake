from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(400, 400)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
  screen.update()
  time.sleep(0.1)
  snake.move()
  if snake.head.distance(food) < 15:
    food.refresh()
    scoreboard.increase_score()
    snake.extend()

  if snake.head.xcor() < -190 or snake.head.xcor() > 190:
      snake.head.goto(-snake.head.xcor(), snake.head.ycor())
    
  if snake.head.ycor() < -190 or snake.head.ycor() > 190:
    snake.head.goto(snake.head.xcor(), -snake.head.ycor())
      
     

  for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
      game_on = False
      scoreboard.game_over()