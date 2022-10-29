from tkinter import *

window = Tk()
window.geometry("500x500")
window.minsize(200,100)
window.maxsize(600,600)

txt = Entry(window,width=20)
txt.place(x=10,y=10)
def click():
    res = "Welcome " + txt.get()
    txt1 = Label(window,text=res)
    txt1.place(x=100,y=70)

btn = Button(window,text='submit',command=click)
btn.place(x=40,y=40)

window.mainloop()