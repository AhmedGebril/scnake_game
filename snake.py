from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.new_segment = []
        self.creat_snake()
        self.head = self.new_segment[0]

    def creat_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.new_segment.append(segment)

    def extend(self):
        # doesn't matter the position it depends on the movement function
        self.add_segment(self.new_segment[-1].position())

    def move(self):
        for segment in range(len(self.new_segment) - 1, 0, -1):
            new_x = self.new_segment[segment - 1].xcor()
            new_y = self.new_segment[segment - 1].ycor()
            self.new_segment[segment].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def Right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def Left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def resetsnake(self):
        for segment in self.new_segment:
            segment.goto(1000, 1000)
        self.new_segment.clear()
        self.creat_snake()
        self.head = self.new_segment[0]
