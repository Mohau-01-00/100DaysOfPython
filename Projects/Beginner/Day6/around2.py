
def turn_right():
 
    turn_left()
    turn_left()
    turn_left()

 

while front_is_clear():
       move()
       if wall_in_front():
          turn_left()
       elif right_is_clear():
           turn_right()