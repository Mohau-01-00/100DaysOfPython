from tkinter import *

window=Tk()
window.title("Mile to Km Converter")
window.minsize(width=300,height=200)
window.config(padx=10,pady=10)


# my_label["text"]="New Text"
# my_label.config(text="New Text")

def button_clicked():
    print("I got clicked")






input=Entry(width=20)
input.grid(column=1,row=0)


my_label=Label(text="Miles",font=("Arial",10,"normal"))
my_label.grid(column=2,row=0)
my_label.config(padx=10,pady=10)

my_label=Label(text="is equal to",font=("Arial",10,"normal"))
my_label.grid(column=0,row=2)
my_label.config(padx=10,pady=10)




button=Button(text="Click Me",command=button_clicked)
button.grid(column=3,row=1)

button=Button(text="Click Me",command=button_clicked)
button.grid(column=2,row=2)


window.mainloop()