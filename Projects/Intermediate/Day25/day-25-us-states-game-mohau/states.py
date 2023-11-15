from turtle import Turtle
from turtle import Screen
import pandas as pd




class States(Turtle):
    
    def __init__(self):
        super().__init__()

        self.data=pd.read_csv('50_states.csv')
        self.states_list=[]
        self.correct_answer=0
        self.turt = Turtle()



    
    def update_title(self):


       self.answer=self.screen.textinput(f"{self.correct_answer}/50 States Correct", 
                                         prompt="Whats another state's name").title()



    def update_map(self):
        for i,rows in self.data.iterrows():
            self.state=rows['state']
            self.x=rows['x']
            self.y=rows['y']
            if self.state==self.answer and self.state not in self.states_list:
                self.correct_answer+=1
                self.states_list.append(self.answer)
                self.display_map()
                print(self.state)
                print(self.x,self.y)
            elif self.answer=="Exit":
                break
            else:
                pass
            

    def display_map(self):
        self.turt.hideturtle()
        self.turt.penup()
        self.turt.goto(self.x,self.y)
        self.turt.write(self.state,move=False, font=('Arial',10,'normal'),align='left')

        


       

    



        

    
     
