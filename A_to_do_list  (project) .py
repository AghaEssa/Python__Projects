import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("My To-Do List")
root.geometry("400x450")
root.config(bg="#f4f4f4")

# Heading
heading = tk.Label(root, text="My Daily Tasks", font=("Arial", 18, "bold"), bg="#f4f4f4", fg="#333")
heading.pack(pady=10)

# Entry field
task_entry = tk.Entry(root, font=("Arial", 14), width=30)
task_entry.pack(pady=10)

# Frame for buttons
btn_frame = tk.Frame(root, bg="#f4f4f4")
btn_frame.pack(pady=5)

# Listbox to show tasks
task_listbox = tk.Listbox(root, font=("Arial", 12), width=40, height=10, selectbackground="#a3d2ca")
task_listbox.pack(pady=10)

# Functions
def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Field", "Please enter a task.")

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected)
    else:
        messagebox.showwarning("No Selection", "Please select a task to delete.")

def clear_all():
    if messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?"):
        task_listbox.delete(0, tk.END)

# Buttons
add_btn = tk.Button(btn_frame, text="Add Task", font=("Arial", 12), bg="#76b5c5", fg="white", width=10, command=add_task)
add_btn.grid(row=0, column=0, padx=5)

del_btn = tk.Button(btn_frame, text="Delete Task", font=("Arial", 12), bg="#e27d60", fg="white", width=12, command=delete_task)
del_btn.grid(row=0, column=1, padx=5)

clear_btn = tk.Button(btn_frame, text="Clear All", font=("Arial", 12), bg="#c94c4c", fg="white", width=10, command=clear_all)
clear_btn.grid(row=0, column=2, padx=5)

# Run   the   app
root.mainloop()
