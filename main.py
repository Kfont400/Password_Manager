from email import message
from tkinter import *
from tkinter import messagebox
import json
# import pyperclip

# ------------------------------- Clear Screen ---------------------------------- #
def clear_output():
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    confirm.config(text='')
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def search():
    try:
        with open('data.json', 'r') as f:
            #reading old data
            data = json.load(f)
            website = data[website_entry.get()]
            email = website['email']
            password = website['password']
            messagebox.showinfo(title='Found',message=f'Email: {email} \nPassword: {password}')
    except(FileNotFoundError, json.decoder.JSONDecodeError):
        messagebox.showerror(title='Erro', message="No Data File Found")
    except KeyError:
        messagebox.showerror(title='Erro', message='No details for this website exists')



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def generate_password():
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbol = '!@#$%^&*+-/._-()[]{}'

    ans = lower + upper + numbers + symbol
    length = random.randint(8,12)
    password = "".join(random.sample(ans, length))

    password_entry.delete(0, END)
    password_entry.insert(0,password)
    # pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    website = website_entry.get()
    email = email_user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': email,
            'password' : password,
        }
    }


    if len(email) == 0 and len(website) == 0 and len(password) == 0:
        messagebox.showerror('Error', 'One or more boxes have not been filled')
    else:
        try:
            with open('data.json', 'r') as f:
                #reading old data
                data = json.load(f)
        except(FileNotFoundError, json.decoder.JSONDecodeError):
            with open('data.json', 'w') as f:
                json.dump(new_data, f, indent=4)
        else:
            #updating old data with new data
            data.update(new_data)

            with open('data.json', 'w') as f:
                #saving updated data
                json.dump(data, f, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height = 200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_entry = Entry(width=33)
website_label.grid(column=0,row=1)
website_entry.grid(column=1 , row=1)
search_website = Button(text='Search', width = 14, command=search)
search_website.grid(column = 2, row=1)
website_entry.focus()

email_user_label = Label(text='Email/Username:')
email_user_entry = Entry(width=52)
email_user_label.grid(column=0, row=2)
email_user_entry.grid(column=1, row=2,columnspan=2)
email_user_entry.insert(0, 'kfont400@gmail.com')

password_label = Label(text='Password:')
password_entry = Entry(width=33)
generate_button = Button(text='Generate Password',command=generate_password)

password_label.grid(column=0, row=3)
password_entry.grid(column=1, row=3)
generate_button.grid(column=2, row=3)

add_button = Button(text='Add',width=28, command=save_info)
add_button.grid(column=1, row=4)
clear_button = Button(text='Clear',width=14, command=clear_output )
clear_button.grid(column=2, row=4)

confirm = Label(text='')
confirm.grid(column=1, row=6)

window.mainloop()
