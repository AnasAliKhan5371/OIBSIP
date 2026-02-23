import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.title("BMI CALCULATOR")
root.geometry("300x350")

# INPUTS
tk.Label(root,text="Weight (kg):").grid(row=0 ,column=0, padx=10,pady=10)
weight_entry=tk.Entry(root)
weight_entry.grid(row=0, column=1)

tk.Label(root,text="Height (M):").grid(row=1 ,column=0, padx=10,pady=10)
height_entry=tk.Entry(root)
height_entry.grid(row=1, column=1)

# CALCULATE BMI
def calculate():
    try:
        # Inputs
        w=float(weight_entry.get())
        h=float(height_entry.get())

        if h<=0 or w<=0:
            messagebox.showerror("Input Error !!! ", "Please enter positive numbers.")
            return

        # BMI
        bmi = w/(h**2)
        if bmi < 18.5:
            res = "Underweight"
            color = "blue"
        elif 18.5 <= bmi < 24.9:
            res = "Normal weight"
            color = "green"
        elif 25.0 <= bmi < 29.9:
            res = "Overweight"
            color = "orange"
        else:
            res = "Obesity"
            color = "red"

        # display
        result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {res}",fg=color)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter numeric values only.")

calc_button=tk.Button(root,text="Calculate BMI", command=calculate)
calc_button.grid(row=2,column=0, columnspan=2, pady=20)

result_label=tk.Label(root,text="Enter details and calculate",font=("Arial",12,"bold"),fg="black")
result_label.grid(row=3,column=0, columnspan=2, pady=10)

root.mainloop()