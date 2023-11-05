from turtle import Turtle
import time

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
    def create_snake(self):
        for pos in START_POSITIONS:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(pos)
            self.segments.append(new_segment)

    def move(self):
        for i in range(len(self.segments) - 1, -1, -1):
            if i == 0:
                self.segments[i].forward(MOVE_DISTANCE)
            else:
                self.segments[i].goto(self.segments[i - 1].pos())

    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def left(self):
        self.segments[0].setheading(180)

    def right(self):
        self.segments[0].setheading(0)


