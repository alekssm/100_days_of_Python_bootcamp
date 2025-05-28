import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_counter():
    global reps
    reps +=1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        main_label.config(text="Long break", fg=RED)
    elif reps % 2 != 0:
        count_down(WORK_MIN * 60)
        main_label.config(text="Work", fg=GREEN)
    else:
        main_label.config(text="Short break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    min_count = math.floor(count / 60)
    sec_count = count % 60
    if sec_count == 0:
        sec_count = "00"
    elif sec_count < 10:
        sec_count = f"0{sec_count}"

    canvas.itemconfig(timer_text, text=f"{min_count}:{sec_count}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    elif count == 0:
        start_counter()

# ---------------------------- UI SETUP ------------------------------- #


def stop_counter():
    pass

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

main_label = tkinter.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 39, "bold"))
main_label.grid(column=1, row=0)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = tkinter.Button(text="Start", command=start_counter, highlightthickness=0)
start_button.grid(column=0, row=2)

tick_label = tkinter.Label(text="✔", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25, "bold"))
tick_label.grid(column=1, row=2)

reset_button = tkinter.Button(text="Reset", command=start_counter, highlightthickness=0)
reset_button.grid(column=2, row=2)




window.mainloop()