from tkinter import *

def reverse():
    s=entry.get()
    s2=''
    for i in range(len(s)-1,-1,-1):
        s2=s2+s[i]
    output.configure(text=s2)
    entry.delete(0,END)


root=Tk()
label=Label(text='Enter a word:')
entry= Entry()
output=Label(font=(8))
btn=Button(text='           Validate             ',command=reverse,bg='#FF0000',fg='white')

label.grid(row=0,column=0, padx=(20, 10), pady=(20, 0))
entry.grid(row=0,column=1, padx=(20, 20), pady=(20, 0))
output.grid(row=1,column=1, padx=(20, 20), pady=(10, 10))
btn.grid(row=2,column=1, padx=(20, 20), pady=(0, 20))




mainloop()
