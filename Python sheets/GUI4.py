from tkinter import *
def sum():
    m= eval(inpt1.get())
    n= eval(inpt2.get())
    s='The Sum is: '+str(m)+' + '+str(n)+' = '+str(m+n)
    outpt.configure(text=s)

root=Tk()

label1=Label(text='Enter the value of M: ',font=(8))
label1.grid(row=0,column=0, padx=(20,10),pady=(20,0))

inpt1=Entry(width = 30,font=(8))
inpt1.grid(row=0,column=1, padx=(10,20),pady=(20,0))

label2=Label(text='Enter the value of N: ',font=(8))
label2.grid(row=1,column=0, padx=(20,10),pady=(0,0))

inpt2=Entry(width = 30,font=(8))
inpt2.grid(row=1,column=1, padx=(10,20),pady=(5,0))

outpt=Label(font=(8))
outpt.grid(sticky='w',row=2,column=1, padx=(20,20),pady=(10,10))

btn=Button(command=sum,width = 30,text='Validate',font=(8))
btn.grid(row=3,column=1, padx=(20,20),pady=(0,10))



mainloop()