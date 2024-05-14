import tkinter as tk
from tkinter import messagebox
import random
import string
from tkinter import ttk

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Password length should be greater than 0")
            return
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for password length")


def copy_to_clipboard():
    password = password_entry.get()
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Copied", "Password has been copied to clipboard")

root = tk.Tk()
root.title("Password Generator")
root.geometry("300x275")

length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="we")

password_label = tk.Label(root, text="Generated Password:")
password_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

password_entry = tk.Entry(root)
password_entry.grid(row=2, column=1, padx=10, pady=10, sticky="we")


copy_button = tk.Button(root, text="Copy", command=copy_to_clipboard)
copy_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="we")

root.mainloop()
