def clear_output():
    website_entry.delete(0, END)
    password_entry.delete(0, END)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def generate_password():
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbol = '!@#$%^&*+-/._-()[]{}'

    ans = lower + upper + numbers + symbol
    length = 9
    password = "".join(random.sample(ans, length))

    password_entry.delete(0, END)
    password_entry.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    with open('saved_passwords.txt', 'a') as f:
        f.write(f'{website_entry.get()} | {email_user_entry.get()} | {password_entry.get()}\n')


# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height = 200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_entry = Entry(width=52)
website_label.grid(column=0,row=1)
website_entry.grid(column=1 , row=1, columnspan=2)
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
clear_button = Button(text='Clear',width=10, command=clear_output )
clear_button.grid(column=2, row=4)


window.mainloop()