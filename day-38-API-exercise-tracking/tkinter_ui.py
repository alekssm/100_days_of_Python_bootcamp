import tkinter as tk
from tkinter import messagebox
from nutritionix_api import fetch_exercises
from sheety_api import log_exercise

GENDER = "Male"
WEIGHT_KG = 70
HEIGHT_CM = 172
AGE = 30

class FitnessApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Workout Logger")

        self.label = tk.Label(root, text="Enter your workout:", font=("Arial", 12))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=50, font=("Arial", 12))
        self.entry.pack(padx=10, pady=5)

        self.submit_btn = tk.Button(root, text="Submit", command=self.handle_submit, font=("Arial", 12))
        self.submit_btn.pack(pady=10)

    def handle_submit(self):
        query = self.entry.get().strip()
        if not query:
            messagebox.showwarning("Input Needed", "Please enter a workout.")
            return

        try:
            exercises = fetch_exercises(query, GENDER, WEIGHT_KG, HEIGHT_CM, AGE)
            for exercise in exercises:
                log_exercise(exercise)
            messagebox.showinfo("Success", f"{len(exercises)} exercises logged.")
            self.entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FitnessApp(root)
    root.mainloop()