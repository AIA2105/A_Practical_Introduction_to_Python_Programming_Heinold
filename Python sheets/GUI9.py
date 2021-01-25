from tkinter import *
from math import gcd,lcm
def sum():
    m= eval(inpt1.get())
    n= eval(inpt2.get())
    s='The Sum is: '+str(m)+' + '+str(n)+' = '+str(m+n)
    outpt.configure(text=s)

def function(x):
    if x=='GCD':
        outpt.configure(text='GCD(M, N) = '+str(gcd(eval(inpt1.get()),eval(inpt2.get()))))
    else:
        outpt.configure(text='LCM(M, N) = '+str(lcm(eval(inpt1.get()),eval(inpt2.get()))))



root=Tk()

label1=Label(text='Enter the value of M: ',font=(8))
label1.grid(row=0,column=0, padx=(20,10),pady=(20,0))

inpt1=Entry(width = 20,font=(8))
inpt1.grid(row=0,column=1, padx=(10,20),pady=(20,0))

label2=Label(text='Enter the value of N: ',font=(8))
label2.grid(row=1,column=0, padx=(20,10),pady=(0,0))

inpt2=Entry(width = 20,font=(8))
inpt2.grid(row=1,column=1, padx=(10,20),pady=(5,0))

label3=Label(text='Choose function: ',font=(8))
label3.grid(sticky='w',row=2,column=0, padx=(20,10),pady=(0,0))

variable = StringVar(root)
variable.set("GCD/LCM") # default value
w = OptionMenu(root, variable, "GCD", "LCM",command=function)
w.grid(row=2,column=1,padx=(10,20),pady=(5,0),sticky="ew")

outpt=Label(font=(8))
outpt.grid(sticky='w',row=3,column=1, padx=(20,20),pady=(10,10))


mainloop()