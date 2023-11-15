import turtle
import pandas as pd

from states import States


states=States()
screen=turtle.Screen()

screen.title("U.S States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)




game_on=True

while game_on:





    states.update_title()
    # states.check_state()
    states.update_map()


turtle.mainloop()
