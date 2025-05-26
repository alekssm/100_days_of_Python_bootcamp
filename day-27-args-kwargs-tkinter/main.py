import tkinter

def button_click ():
    user_input = input_box.get()
    my_label["text"] = user_input

window = tkinter.Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="Label", font=("Arial", 24))
my_label.grid(column=0, row=0)

button = tkinter.Button(text="Click me", command=button_click)
button.grid(column=1, row=1)

button2 = tkinter.Button(text="Click me", command=button_click)
button2.grid(column=3, row=0)

input_box = tkinter.Entry(width=10)
input_box.grid(column=4, row=3)



window.mainloop()