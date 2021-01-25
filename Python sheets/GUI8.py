from tkinter import *
def div():
    m= eval(inpt1.get())
    s=''
    for i in range(1,m+1):
        if m%i==0:
            s=s+str(i)+'   '
    label3.configure(text=s)

root=Tk()

label1=Label(text='Enter the value of N: ',font=(8))
label1.grid(row=0,column=0, padx=(20,10),pady=(20,0))

inpt1=Entry(width = 20,font=(8))
inpt1.grid(row=0,column=1, padx=(10,20),pady=(20,0))

label2=Label(text='The divisors of N: ',font=(8))
label2.grid(sticky='w',row=1,column=0, padx=(20,10),pady=(0,0))

label3=Label(font=(8))
label3.grid(row=1,column=1, padx=(20,10),pady=(0,0))

btn=Button(command=div,width = 20,text='Validate',font=(8))
btn.grid(row=2,column=1, padx=(20,20),pady=(0,30))



mainloop()