from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("square")
        self.penup()
        self.x_move = 300
        self.move_speed = 0.1
        self.goto(300, 0)

    def move(self):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE
        new_y = 0
        self.goto(new_x, new_y)

    def add_car(self):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color(random.choice(COLORS))
        new_segment.penup()
        new_segment.goto(random.randint(-280, 280), -360)
