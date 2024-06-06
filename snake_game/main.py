import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
sb = ScoreBoard()


screen.listen()

screen.onkey(snake.up, "w")
screen.onkey(snake.right, "d")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # eating food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        sb.increase_score()

    # hitting wall
    if snake.segments[0].xcor() > 290 or snake.segments[0].ycor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() < -290:
        game_on = False
        sb.gameover()

    # hitting tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_on = False
            sb.gameover()


screen.exitonclick()
