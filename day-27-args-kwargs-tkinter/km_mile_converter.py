import tkinter

def convert_to_miles():
    user_input = float(miles_input_box.get())
    km = str(round(user_input * 1.60934, 2))
    converted_miles.config(text=km)


window = tkinter.Tk()
window.title("Widget Examples")
window.minsize()
window.config(padx=20, pady=20)

label = tkinter.Label(text="is equal to")
label.grid(column=0, row=1)

miles_input_box = tkinter.Entry(width=5)
miles_input_box.insert(tkinter.END, string="0")
miles_input_box.focus()
miles_input_box.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

converted_miles = tkinter.Label(text="0")
converted_miles.grid(column=1, row=1)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

button = tkinter.Button(text="Calculate", command=convert_to_miles)
button.grid(column=1, row=2)


window.mainloop()