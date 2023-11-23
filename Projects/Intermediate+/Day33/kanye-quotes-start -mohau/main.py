from tkinter import *
import requests
import random



def get_quote():
    response=requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data=response.json()
    quote=data['quote']

    canvas.itemconfig(quote_text,text=quote)

    


    print(quote)
    print(data)
    #Write your code here.



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=150, height=208)
background_img = PhotoImage(file="background.png")
canvas.create_image(75, 104, image=background_img)
quote_text = canvas.create_text(72, 102, text="Kanye Quote Goes HERE", width=110, font=("Arial", 11, "bold"), fill="black")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0,borderwidth=1,  command=get_quote)
kanye_button.grid(row=1, column=0)
get_quote()


window.mainloop()