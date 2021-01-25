from tkinter import *
def welcome():
    outpt.configure(text='Welcome '+inpt1.get()+' !')

root=Tk()

label1=Label(text='Enter your name: ',font=(8))
label1.grid(row=0,column=0, padx=(20,0),pady=(20,0))

inpt1=Entry(width = 20,font=(8))
inpt1.grid(row=0,column=1, padx=(10,20),pady=(20,10))

btn=Button(command=welcome,width = 20,text='Validate',font=(8))
btn.grid(row=1,column=1, padx=(20,20),pady=(0,10))

outpt=Label(font=(8))
outpt.grid(sticky='w',row=2,column=1, padx=(20,20),pady=(10,20))





mainloop()