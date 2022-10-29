from tkinter import *
from tkinter.ttk import *

window = Tk()
window.geometry("500x500")
window.minsize(200,100)
window.maxsize(600,600)

combo = Combobox(window)
combo['values'] = (1,2,3,4,5,'text')
combo.current(1)
combo.place(x=50,y=100)

txt = Entry(window,width=20,state="disable")
txt.place(x=10,y=10)
#txt.focus()
def click():
    res = "Welcome " + txt.get()
    txt1 = Label(window,text=res)
    txt1.place(x=100,y=70)

btn = Button(window,text='submit',command=click)
btn.place(x=40,y=40)



window.mainloop()