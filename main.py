### Day 20. Project - snake game

from turtle import Screen, Turtle
import time

from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.update()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # for i in range(len(snake) - 1, -1, -1):
    #     print (f"i: {i}")
    #     if i == 0:
    #         snake[i].forward(20)
    #     else:
    #         snake[i].goto(snake[i-1].pos())

    # for segment in snake:
    #     segment.forward(20)


screen.exitonclick()
