import random
from tkinter import *
from tkinter.messagebox import showinfo


window=Tk()
window.title("Password Generator")
window.config(bg='#34eb4c')

def generate():
        string=entry.get()
        length=int(entry2.get())
        password=''
        for i in range(length):
            password=password+random.choice(string)
        showinfo("Generated password",f"Your Password:{password}")




label=Label(window,text="Enter String:")
label.grid(row=0,column=0,padx=8,pady=9)

entry=Entry(window)
entry.grid(row=0,column=1,padx=9)


label1=Label(window,text="Enter the password length:")
label1.grid(row=1,column=0,padx=8,pady=8)

entry2=Entry(window)
entry2.grid(row=1,column=1,padx=8)

button=Button(window,text="Generating Password",command=generate)
button.grid(row=2,column=0,columnspan=2,padx=8)


window.mainloop()