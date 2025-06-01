from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)


# ---------------------------- SEARCH ENTRY ------------------------------- #
def search_entry():
    website = website_input_box.get()

    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showwarning(message="No Data File Found.")
    else:
        try:
            email, password = data[website].values()
        except KeyError:
            messagebox.showwarning(message="No Logins found for this website.")
        else:
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")



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

    new_data = {
        website: {
            "email": email_username,
            "password": password
        }
    }

    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showwarning(message="Fill all of the fields!")
    else:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)

        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)

        else:
            data.update(new_data)
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)

        finally:
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

website_input_box = Entry(width=20)
website_input_box.insert(END, string="")
website_input_box.focus()
website_input_box.grid(column=1, row=1)

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

search_button = Button(text="Search", command=search_entry, width=11)
search_button.grid(column=2, row=1)



window.mainloop()