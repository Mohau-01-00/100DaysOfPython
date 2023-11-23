
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    letters_list=[random.choice(letters) for char in range(nr_letters)]
    symbols_list=[random.choice(symbols) for char in range(nr_symbols)]
    numbers_list=[random.choice(numbers) for char in range(nr_numbers)]

    password_list=letters_list+symbols_list+numbers_list
    random.shuffle(password_list)

    password = "".join(password_list)

    
    password_entry.insert(0,password)
    #copy password to clipboard
    pyperclip.copy(password)


#-----------------------------FIND PASSWORD --------------------------------#


def find_password():


    web_text=web_entry.get().title()

    try:

        with open("data.json") as data_file:
            data=json.load(data_file)
            print(web_text)
    except FileNotFoundError:
       messagebox.showinfo(title="Error",message="No Data File Found.")
    else:
            if web_text in data:
                email=data[web_text]["email"]
                password=data[web_text]["password"]
                messagebox.showinfo(title=web_text,message=f"Email :{email}\nPassword :{password}")

            else:
                messagebox.showinfo(title="Error",message=f"No Details for {web_text} exist")
                



# ---------------------------- SAVE PASSWORD ------------------------------- #
def delete_text():
    web_entry.delete(0,END)
 
    password_entry.delete(0,END)


def write_to_file():
    
    

    web_text=web_entry.get().title()
    email=email_entry.get()
    password=password_entry.get()
    new_data={
        web_text:{
            "email":email,
            "password":password,
        }

    }


    if len(web_text)<=0 or len(password)<=0:
        messagebox.showerror(title="Error",message="Text Box cannot be empty")

    else:
        try:
            with open("data.json","r") as data_file:
                # Try Reading old data with the code above  
                # below is to assign a variable data to append new_data to data in else:
                data=json.load(data_file)

        except FileNotFoundError:
                with open("data.json","w") as data_file:
            
                   json.dump(new_data,data_file,indent=4)
                
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json","w") as data_file:
                #Saving updated data
                json.dump(data,data_file,indent=4)
        finally:
            delete_text()



# ---------------------------- UI SETUP ------------------------------- #
FONT_NAME = "Courier"

window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)


canvas=Canvas()
lock_img=PhotoImage(file="logo.png")
canvas.create_image(170,130,image=lock_img)
canvas.grid(column=0, row=0, columnspan=3)

#Labels
web_label=Label(text="Website :",font=(FONT_NAME,10))
web_label.grid(row=1,column=0)
email_label=Label(text="Email/Username :",font=(FONT_NAME,10))
email_label.grid(row=2,column=0)
password_label=Label(text="Password :",font=(FONT_NAME,10))
password_label.grid(row=3,column=0)


#Entries
web_entry = Entry(width=23)
web_entry.grid(row=1,column=1)
web_entry.focus()
email_entry = Entry(width=42)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0, "mohaumasukela@gmail.com")
password_entry = Entry(text="",font=("Arial",10,"normal"),width=20)
password_entry.grid(row=3,column=1)

#Buttons
search_button=Button(text="Search",width=14,command=find_password)
search_button.grid(row=1,column=2)
password_button=Button(text="Generate Password",command=generate_password)
password_button.grid(row=3,column=2)
add_button=Button(text="Add",width=35,command=write_to_file)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()