from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"



#---------------------UI-SETUP--------------------------

window=Tk()
window.title("Flash Card App")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)


canvas=Canvas(width=820,height=526)
card_back=PhotoImage(file="images/card_back.png")
canvas.create_image(410,260,image=card_back)
canvas.grid(row=0,column=0)

right_img=PhotoImage(file="images/right.png")
r_button=Button(image=right_img)
r_button.grid(row=1,column=0)



window.mainloop()