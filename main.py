import tkinter as tk
from tkinter import  messagebox
root=tk.Tk()
root.title("To-Do-List")
frame=tk.Frame(root)
frame.pack()
def add_task():
    task=task_add.get()
    if task!="":
        todo_box.insert(tk.END, task)
        task_add.delete(0, tk.END)
    else:
        tk.messagebox.showwarning(title="Warning!",message="You must enter a task.")
def delete():
    try:
        task = todo_box.curselection()
        todo_box.delete(task)
    except:
        tk.messagebox.showwarning(title="Warning!", message="You must select a task.")
def update():
    task=todo_box.curselection()
    new_task=task_add.get()
    if task and new_task !="":
        todo_box.delete(task)
        todo_box.insert(tk.END, new_task)
        task_add.delete(0, tk.END)
    else:
        tk.messagebox.showwarning(title="Warning!", message="You must select a task.")
def mark():
    try:
        selected_task = todo_box.curselection()
        todo_box.itemconfig(selected_task, {'bg': 'light green'})
    except:
        messagebox.showwarning("Warning", "Please select a task to mark.")
def unmark():
    try:
        selected_task = todo_box.curselection()
        todo_box.itemconfig(selected_task, {'bg': 'red'})
    except:
        messagebox.showwarning("Warning", "Please select a task to unmark.")
todo_box=tk.Listbox(frame,height=20,width=50)
todo_box.pack(side=tk.LEFT)

scroll=tk.Scrollbar(frame)
scroll.pack(side=tk.RIGHT,fill=tk.Y)
todo_box.config(yscrollcommand=scroll.set)
scroll.config(command=todo_box.yview)
task_add=tk.Entry(root,width=40)
task_add.pack(pady=5)
task_add_button=tk.Button(root,text="Click to add task".upper(),background="white",width=48,command=add_task)
task_add_button.pack(pady=5)
task_delete_button=tk.Button(root,text="Click to delete task".upper(),background="white",width=48,command=delete)
task_delete_button.pack(pady=5)
task_update_button=tk.Button(root,text="Click to update task".upper(),background="white",width=48,command=update)
task_update_button.pack(pady=5)
task_mark_button=tk.Button(root,text="Click to mark task".upper(),background="white",width=48,command=mark)
task_mark_button.pack(pady=5)
task_unmark_button=tk.Button(root,text="Click to unmark task".upper(),background="white",width=48,command=unmark)
task_unmark_button.pack(pady=5)
root.mainloop()