from tkinter import *
def sum():
    inpt2.delete(0,END)
    m= eval(inpt1.get())
    inpt2.insert(0,str(2*m))

root=Tk()

label1=Label(text='Enter the value of N: ',font=(8))
label1.grid(row=0,column=0, padx=(20,10),pady=(20,0))

inpt1=Entry(width = 20,font=(8))
inpt1.grid(row=0,column=1, padx=(10,20),pady=(20,0))

label2=Label(text='Here is thr double 2*N: ',font=(8))
label2.grid(row=1,column=0, padx=(20,10),pady=(0,0))

inpt2=Entry(width = 20,font=(8))
inpt2.grid(row=1,column=1, padx=(10,20),pady=(5,0))

btn=Button(command=sum,width = 20,text='Validate',font=(8))
btn.grid(row=2,column=1, padx=(20,20),pady=(0,30))



mainloop()