
from turtle import Turtle,Screen


#triangle,square,pentagon,hexagon,heptagon,octagon,nonagon,decagon
tim=Turtle()


def triangle():
    for _ in range(3):
        tim.forward(100)
        tim.right(120)
        tim.speed(1)

def square():
    for _ in range(4):
        tim.forward(100)
        tim.right(90)

def pentagon():
    for _ in range(5):
        tim.forward(100)
        tim.right(72)

def hexagon():
    for _ in range(6):
        tim.forward(100)
        tim.right(60)

def heptagon():
    for _ in range(7):
        tim.forward(100)
        tim.right(51.4)

def octagon():
    for _ in range(8):
        tim.forward(100)
        tim.right(45)
   
def nanogon():
    for _ in range(9):
        tim.forward(100)
        tim.right(40)

def decaogon():
    for _ in range(10):
        tim.forward(100)
        tim.right(36)



triangle()
square()
pentagon()
hexagon()
heptagon()
nanogon()
decaogon()



















my_screen=Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
