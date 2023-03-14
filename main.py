import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.add_car()
    car.add_car()
    car.move()

    if car.distance(player) < 50:
        scoreboard.game_over()

    if player.ycor() > player.finish_line:
        player.reset_position()
        scoreboard.add_point()
