from tkinter import *

window=Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)

my_label=Label(text="I am a Label",font=("Arial",24,"bold"))
my_label.pack()

# my_label["text"]="New Text"
# my_label.config(text="New Text")

def button_clicked():
    print("I got clicked")
    # my_label.config(text="Button got Clicked")
    new_text=input.get()
    my_label.config(text=new_text)



button=Button(text="Click Me",command=button_clicked)
button.pack()

input=Entry(width=20)
input.pack()
# input.get()

window.mainloop()