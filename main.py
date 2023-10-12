from tkinter import *
from tkinter import  messagebox
from random import randint
root=Tk()
root.title('PASSWORD GENERATOR')
root.geometry("500x300")
my_password=chr(randint(33,126))
def p_gen():
    p_entry.delete(0,END)
    lenght=int(my_entry.get())
    my_pass=''
    for i in range(lenght):
        my_pass += chr(randint(33, 126))
    p_entry.insert(0,my_pass)
def copy():
    root.clipboard_clear()
    root.clipboard_append(p_entry.get())
    messagebox.showinfo(title="successful!", message="Your text copied")

lb=LabelFrame(root,text="How Many Characters?")
lb.pack(pady=20)
my_entry=Entry(lb,font=("Helvetica",24))
my_entry.pack(pady=20,padx=20)
p_entry=Entry(root,text='',font=("Helvetica",24),bd=0,bg="systembuttonface")
p_entry.pack(pady=20)

my_frame=Frame(root)
my_frame.pack(pady=20)
my_button=Button(my_frame,text="Generate Strong Password",command=p_gen)
my_button.grid(row=0,column=0,padx=10)
copy_button=Button(my_frame,text="Copy To Clipboard",command=copy)
copy_button.grid(row=0,column=1,padx=10)


root.mainloop()