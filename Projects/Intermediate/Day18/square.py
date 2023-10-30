
from turtle import Turtle, Screen

tim=Turtle()

tim.color("CadetBlue")

def square():
    for _ in range(4):
        tim.forward(100)
        tim.left(90)
   


def dashed_line():
    for _ in range(15):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()



  


dashed_line()










my_screen=Screen()
print(my_screen.canvheight)
my_screen.exitonclick()




