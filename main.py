from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from ScoreBoard import Score


screen = Screen()
screen.setup(width=600, height=600)
screen.title("snake game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food=Food()
score=Score()

screen.listen()
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.Left, key="Left")
screen.onkey(fun=snake.Right, key="Right")

is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()
    if snake.head.xcor()>280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        snake.resetsnake()
        score.resetScore()


    for segment in snake.new_segment[1:]:
        if snake.head.distance(segment)<10:
            snake.resetsnake()
            score.resetScore()


screen.exitonclick()
