from tkinter import *
def sum():
    n= eval(inpt.get())
    s=''
    sum=0
    for i in range (1,n):
        s=s+str(i)+' + '
        sum=sum+i
    sum=sum+n
    s=s+str(n)+' = '+str(sum)
    outpt.configure(text=s)

root=Tk()

label1=Label(text='Enter value of integer N: ',font=(8))
label1.grid(row=0,column=0, padx=(20,10),pady=(20,0))

inpt=Entry(width = 30,font=(8))
inpt.grid(row=0,column=1, padx=(10,20),pady=(20,0))

outpt=Label(font=(8))
outpt.grid(sticky='w',row=1,column=1, padx=(20,20),pady=(10,10))

btn=Button(command=sum,width = 30,text='Validate',font=(8))
btn.grid(row=2,column=1, padx=(20,20),pady=(0,10))



mainloop()