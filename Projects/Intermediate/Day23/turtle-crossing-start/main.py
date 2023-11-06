import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Racer")
screen.tracer(0)



player=Player()
car_manager=CarManager()
scorebord=Scoreboard()


screen.listen()
screen.onkey(player.move_up, "Up")


game_is_on = True
loop_count=0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player)<20:
            game_is_on=False
            scorebord.game_over()


    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scorebord.increase_level()





screen.exitonclick()