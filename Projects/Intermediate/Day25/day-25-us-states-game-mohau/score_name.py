import turtle
import pandas as pd




class States(turtle):
    def __init__(self):
        super().__init__()

        self.data=pd.read_csv('50_states.csv')
        self.states_list=[]

    

def check_state(self,answer):
    for state in self.data['states']:
        if state==answer:
            # screen.write(f"Score: {self.score} High Score:{self.high_score}", align=ALIGNMENT, font=FONT)
            print("Well Done")
    

    
     
