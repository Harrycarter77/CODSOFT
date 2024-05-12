import tkinter as tk
from tkinter import ttk, messagebox
import json

class TodoListApp(tk.Tk):
    def __init__(root):
        super().__init__()

        root.title("Todo List App")
        root.geometry("1200x800")
        
        root.task_input = ttk.Entry(root, font=(
            "TkDefaultFont", 16), width=30, style="Custon.TEntry")
        root.task_input.pack(pady=10)

        
        root.task_input.insert(0, "Enter your schedule here...")

        root.task_input.bind("<FocusIn>", root.clear_placeholder)
        
        root.task_input.bind("<FocusOut>", root.restore_placeholder)

        
        ttk.Button(root, text="Add", command=root.add_task).pack(pady=5)

        
        root.task_list = tk.Listbox(root, font=(
            "TkDefaultFont", 16), height=10, selectmode=tk.NONE)
        root.task_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        ttk.Button(root, text="Done", style="success.TButton",
                   command=root.mark_done).pack(side=tk.LEFT, padx=10, pady=10)
        ttk.Button(root, text="Delete", style="danger.TButton",
                   command=root.delete_task).pack(side=tk.RIGHT, padx=10, pady=10)
        
        
        ttk.Button(root, text="View Stats", style="info.TButton",
                   command=root.view_stats).pack(side=tk.BOTTOM, pady=10)
        
        root.load_tasks()
    
    def view_stats(root):
        done_count = 0
        total_count = root.task_list.size()
        for i in range(total_count):
                done_count += 1
        messagebox.showinfo("Task Statistics", f"Total tasks: {total_count}\nCompleted tasks: {done_count}")

    def add_task(root):
        task = root.task_input.get()
        if task != "Enter your schedule here...":
            root.task_list.insert(tk.END, task)
            root.task_list.itemconfig(tk.END, fg="orange")
            root.task_input.delete(0, tk.END)
            root.save_tasks()

    def mark_done(root):
        task_index = root.task_list.curselection()
        if task_index:
            root.task_list.itemconfig(task_index, fg="green")
            root.save_tasks()
    
    def delete_task(root):
        task_index = root.task_list.curselection()
        if task_index:
            root.task_list.delete(task_index)
            root.save_tasks()
    
    def clear_placeholder(root, event):
        if root.task_input.get() == "Enter your schedule here...":
            root.task_input.delete(0, tk.END)
            root.task_input.configure(style="TEntry")

    def restore_placeholder(root, event):
        if root.task_input.get() == "":
            root.task_input.insert(0, "Enter your schedule here...")
            root.task_input.configure(style="Custom.TEntry")

    def load_tasks(root):
        try:
            with open("tasks.json", "r") as f:
                data = json.load(f)
                for task in data:
                    root.task_list.insert(tk.END, task["text"])
                    root.task_list.itemconfig(tk.END)
        except FileNotFoundError:
            pass
    
    def save_tasks(root):
        data = []
        for i in range(root.task_list.size()):
            text = root.task_list.get(i)
            data.append({"text": text})
        with open("tasks.json", "w") as f:
            json.dump(data, f)

if __name__ == '__main__':
    app = TodoListApp()
    app.mainloop()