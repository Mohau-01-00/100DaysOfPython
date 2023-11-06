from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move_up(self):
        new_y=self.ycor()+MOVE_DISTANCE
        self.goto(self.xcor(),new_y)


    def is_at_finish_line(self):
        if self.ycor()>FINISH_LINE_Y:
            return True
        else:
            return False
        
    def go_to_start(self):

        self.goto(STARTING_POSITION)

