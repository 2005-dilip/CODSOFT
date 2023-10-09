import tkinter as tk
calculation=""
def add_to_cal(symbol):
    global calculation
    calculation +=str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)

def evaluate_cal():
    global calculation
    try:
        calculation=str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,"Error")
def clear_field():
    global  calculation
    calculation=""
    text_result.delete(1.0,"end")

root=tk.Tk()
root.geometry("300x275")
text_result=tk.Text(root,height=2,width=16,font=("Arial",24))
text_result.grid(columnspan=5)
b1=tk.Button(root,text="1",command=lambda : add_to_cal(1),width=5,font=("Arial",14))
b1.grid(row=2,column=1)
b2=tk.Button(root,text="2",command=lambda : add_to_cal(2),width=5,font=("Arial",14))
b2.grid(row=2,column=2)
b3=tk.Button(root,text="3",command=lambda : add_to_cal(3),width=5,font=("Arial",14))
b3.grid(row=2,column=3)
b4=tk.Button(root,text="4",command=lambda : add_to_cal(4),width=5,font=("Arial",14))
b4.grid(row=3,column=1)
b5=tk.Button(root,text="5",command=lambda : add_to_cal(5),width=5,font=("Arial",14))
b5.grid(row=3,column=2)
b6=tk.Button(root,text="6",command=lambda : add_to_cal(6),width=5,font=("Arial",14))
b6.grid(row=3,column=3)
b7=tk.Button(root,text="7",command=lambda : add_to_cal(7),width=5,font=("Arial",14))
b7.grid(row=4,column=1)
b8=tk.Button(root,text="8",command=lambda : add_to_cal(8),width=5,font=("Arial",14))
b8.grid(row=4,column=2)
b9=tk.Button(root,text="9",command=lambda : add_to_cal(9),width=5,font=("Arial",14))
b9.grid(row=4,column=3)
b0=tk.Button(root,text="0",command=lambda : add_to_cal(0),width=5,font=("Arial",14))
b0.grid(row=5,column=2)
bplus=tk.Button(root,text="+",command=lambda : add_to_cal("+"),width=5,font=("Arial",14))
bplus.grid(row=2,column=4)
bminus=tk.Button(root,text="-",command=lambda : add_to_cal("-"),width=5,font=("Arial",14))
bminus.grid(row=3,column=4)
bmul=tk.Button(root,text="*",command=lambda : add_to_cal("*"),width=5,font=("Arial",14))
bmul.grid(row=4,column=4)
bdiv=tk.Button(root,text="/",command=lambda : add_to_cal("/"),width=5,font=("Arial",14))
bdiv.grid(row=5,column=4)
bopen=tk.Button(root,text="(",command=lambda : add_to_cal("("),width=5,font=("Arial",14))
bopen.grid(row=5,column=1)
bclose=tk.Button(root,text=")",command=lambda : add_to_cal(")"),width=5,font=("Arial",14))
bclose.grid(row=5,column=3)
bclear=tk.Button(root,text="C",command=clear_field,width=11,font=("Arial",14))
bclear.grid(row=6,column=1,columnspan=2)
bequal=tk.Button(root,text="=",command=evaluate_cal,width=11,font=("Arial",14))
bequal.grid(row=6,column=3,columnspan=2)

root.mainloop()