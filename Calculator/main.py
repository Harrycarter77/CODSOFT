import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")
        return "Error"

def calculate():
    operation = opr_var.get()
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())

    if operation == 'Add':
        result = add(num1, num2)
    elif operation == 'Subtract':
        result = sub(num1, num2)
    elif operation == 'Multiply':
        result = multiply(num1, num2)
    elif operation == 'Divide':
        result = divide(num1, num2)

    label_result.config(text="Result: " + str(result))

root = tk.Tk()
root.title("Calculator")
root.geometry("300x275")


tk.Label(root, text="Number 1:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_num1 = tk.Entry(root)
entry_num1.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Number 2:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_num2 = tk.Entry(root)
entry_num2.grid(row=2, column=1, padx=5, pady=5)

opr_var = tk.StringVar()
opr_var.set("Add")
operations = ['Add', 'Subtract', 'Multiply', 'Divide']
opr_menu = tk.OptionMenu(root, opr_var, *operations)
opr_menu.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")
        return "Error"

def calculate():
    operation = opr_var.get()
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())

    if operation == 'Add':
        result = add(num1, num2)
    elif operation == 'Subtract':
        result = sub(num1, num2)
    elif operation == 'Multiply':
        result = multiply(num1, num2)
    elif operation == 'Divide':
        result = divide(num1, num2)

    label_result.config(text="Result: " + str(result))

root = tk.Tk()
root.title("Calculator")
root.geometry("300x275")

tk.Label(root, text="Number 1:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Number 2:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=5, pady=5)

opr_var = tk.StringVar()
opr_var.set("Add")
operations = ['Add', 'Subtract', 'Multiply', 'Divide']
opr_menu = tk.OptionMenu(root, opr_var, *operations)
opr_menu.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

calc_button = tk.Button(root, text="Calculate", command=calculate)
calc_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

label_result = tk.Label(root, text="")
label_result.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()

label_result = tk.Label(root, text="")
label_result.grid(row=3, column=0, columnspan=2, padx=5, pady=5)



calc_button = tk.Button(root, text="Calculate", command=calculate)
calc_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)



root.mainloop()
