import tkinter as tk
from tkinter import messagebox
import csv
import os

def save_contact():
    fname = fname_entry.get()
    lname = lname_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    if not fname or not lname or not phone or not email or not address:
        messagebox.showwarning("Warning", "All fields must be filled out")
        return

    info = [fname, lname, phone, email, address]
    with open('info.csv', 'a', newline="") as w:
        cw = csv.writer(w)
        cw.writerow(info)
    
    clear_entries()
    messagebox.showinfo("Saved", "Contact information saved successfully")

def search_contact():
    search_text = search_entry.get()
    found = False
    if not search_text:
        messagebox.showwarning("Warning", "Please enter a last name to search")
        return

    result_text.set("")  # Clear previous search result
    if os.path.exists('info.csv'):
        with open('info.csv', 'r') as r:
            cr = csv.reader(r)
            for row in cr:
                if row[1].lower() == search_text.lower():
                    result_text.set(f"First Name: {row[0]}\nLast Name: {row[1]}\nPhone Number: {row[2]}\nEmail: {row[3]}\nAddress: {row[4]}")
                    found = True
                    break
    if not found:
        result_text.set("Contact not found")

def clear_entries():
    fname_entry.delete(0, tk.END)
    lname_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def delete_contact():
    search_text = search_entry.get()
    if not search_text:
        messagebox.showwarning("Warning", "Please enter a last name to delete")
        return

    temp_file = 'temp_info.csv'
    with open('info.csv', 'r') as r, open(temp_file, 'w', newline="") as w:
        cr = csv.reader(r)
        cw = csv.writer(w)
        for row in cr:
            if row[1].lower() != search_text.lower():
                cw.writerow(row)
    os.remove('info.csv')
    os.rename(temp_file, 'info.csv')
    messagebox.showinfo("Deleted", "Contact deleted successfully")
    clear_entries()

root = tk.Tk()
root.title("Contact Book")
root.geometry("300x325")

tk.Label(root, text="Enter First Name").grid(row=0, column=0, sticky=tk.W)
fname_entry = tk.Entry(root)
fname_entry.grid(row=0, column=1)

tk.Label(root, text="Enter Last Name").grid(row=1, column=0, sticky=tk.W)
lname_entry = tk.Entry(root)
lname_entry.grid(row=1, column=1)

tk.Label(root, text="Enter Phone Number").grid(row=2, column=0, sticky=tk.W)
phone_entry = tk.Entry(root)
phone_entry.grid(row=2, column=1)

tk.Label(root, text="Enter Email").grid(row=3, column=0, sticky=tk.W)
email_entry = tk.Entry(root)
email_entry.grid(row=3, column=1)

tk.Label(root, text="Enter Address").grid(row=4, column=0, sticky=tk.W)
address_entry = tk.Entry(root)
address_entry.grid(row=4, column=1)

tk.Button(root, text="Save", command=save_contact).grid(row=5, column=0, pady=5)
tk.Button(root, text="Cancel", command=clear_entries).grid(row=5, column=1, pady=5)

tk.Label(root, text="Search by Last Name").grid(row=6, column=0, sticky=tk.W)
search_entry = tk.Entry(root)
search_entry.grid(row=6, column=1)

tk.Button(root, text="Search", command=search_contact).grid(row=7, column=0, pady=5)
tk.Button(root, text="Delete", command=delete_contact).grid(row=7, column=1, pady=5)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.grid(row=8, column=0, columnspan=2)

root.mainloop()
