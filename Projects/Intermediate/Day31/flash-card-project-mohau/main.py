from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
  data=pd.read_csv("data/words_to_learn.csv")

except FileNotFoundError:

   data=pd.read_csv("data/french_words.csv")

to_learn=data.to_dict(orient="records")

current_card={}
#to delete
print(to_learn)


#--------------------Change-Word-----------------------

def french_card():

    #current_card is the nested dictionary in to_learn e.g {'French': 'place', 'English': 'square'}
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)

    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=card_front)
    #below to delete
    # print(f" french_card(){current_card}")
    flip_timer=window.after(3000,english_card)
    

def english_card():
    global current_card

    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=card_back)



def remove_card():
    global current_card
    print(current_card)
    to_learn.remove(current_card)

    print(to_learn)
    data = pd.DataFrame.from_dict(to_learn) 
    data.to_csv("data/words_to_learn.csv", index=False)
    print(data)
    french_card()


#---------------------UI-SETUP--------------------------

window=Tk()
window.title("Flash Card App")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)


flip_timer=window.after(3000,func=english_card)
#The below width and height usually corresponds with the image size 
canvas=Canvas(width=430,height=280,bg=BACKGROUND_COLOR,highlightthickness=0)
card_back=PhotoImage(file="images/card_back.png")
card_front=PhotoImage(file="images/card_front.png")
#The below values just move the image up/down or left/right. They do not re-size image
card_background=canvas.create_image(220,143,image=card_front)
card_title=canvas.create_text(200,72,text="Title",fill="Black",font=("Ariel",20,"italic"))
card_word=canvas.create_text(200,150,text="word",fill="Black",font=("Ariel",40,"bold"))
canvas.grid(row=0,column=0,columnspan=2)


#Buttons
right_img=PhotoImage(file="images/right.png")
r_button=Button(image=right_img,borderwidth=0,command=remove_card)
r_button.grid(row=1,column=0)

wrong_img=PhotoImage(file="images/wrong.png")
w_button=Button(image=wrong_img,borderwidth=0,command=french_card)
w_button.grid(row=1,column=1)

#to automatically display next card instead of placeholders named Title and word on card
french_card()



window.mainloop()