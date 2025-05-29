from tkinter import *
from tkinter import messagebox
import random
import pyperclip

window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for i in range(nr_letters)]

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_numbers + password_letters + password_symbols


    random.shuffle(password_list)

    password = "".join(password_list)

    return password

def fill_password():
    password = generate_password()
    password_input_box.delete(0, END)
    password_input_box.insert(END, string=password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input_box.get()
    email_username = username_input_box.get()
    password = password_input_box.get()

    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showwarning(message="Fill all of the fields!")
    else:
        confirmed = messagebox.showinfo(message=f"Confirm if you want to proceed:\nWebsite: {website}\n"
                                  f"Email: {email_username}\nPassword: {password}")
        if confirmed:
            with open("data.txt", "a") as f:
                f.write(f"{website} | {email_username} | {password}\n")

            website_input_box.delete(0, END)
            username_input_box.delete(0, END)
            username_input_box.insert(END, string="testemail@gmail.com")
            password_input_box.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
canvas = Canvas(width=200, height=200)
padlock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input_box = Entry(width=35)
website_input_box.insert(END, string="")
website_input_box.focus()
website_input_box.grid(column=1, row=1, columnspan=2)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

username_input_box = Entry(width=35)
username_input_box.insert(END, string="testemail@gmail.com")
username_input_box.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_input_box = Entry(width=20)
password_input_box.insert(END, string="")
password_input_box.grid(column=1, row=3)

password_button = Button(text="Generate password", command=fill_password, width=11)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", command=save_password, width=33)
add_button.grid(column=1, row=4, columnspan=2)





window.mainloop()