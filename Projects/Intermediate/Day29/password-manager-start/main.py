
from tkinter import *
from tkinter import messagebox
import random
import pyperclip


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
    pyperclip.copy(password)





# ---------------------------- SAVE PASSWORD ------------------------------- #
def delete_text():
    web_entry.delete(0,END)
 
    password_entry.delete(0,END)


def write_to_file():
    
    

    web_label_text=web_entry.get()
    email_entry_text=email_entry.get()
    password_entry_text=password_entry.get()


    if len(web_label_text)<=0 or len(password_entry_text)<=0:
        messagebox.showerror(title="Error",message="Text Box cannot be empty")

    else:



        is_ok=messagebox.askokcancel(title=web_label_text,message=f"These are the details entered: \nEmail:{email_entry_text}"
        f"\nPassword: {password_entry_text}\nIs it ok to save?")
        if is_ok:
            with open("myfile.txt","a") as file:
                
                file.write(f"{web_label_text}|{email_entry_text}|{password_entry_text}\n")
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
web_entry = Entry(width=42)
web_entry.grid(row=1,column=1,columnspan=2)
web_entry.focus()
email_entry = Entry(width=42)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0, "mohaumasukela@gmail.com")
password_entry = Entry(text="",font=("Arial",10,"normal"),width=20)
password_entry.grid(row=3,column=1)

#Buttons
password_button=Button(text="Generate Password",command=generate_password)
password_button.grid(row=3,column=2)
add_button=Button(text="Add",width=36,command=write_to_file)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()