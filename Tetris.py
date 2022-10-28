from tkinter import *

window = Tk()
window.geometry('500x500+500+100')
window.title("Hello my friend")
paragraphe = Label(window, text="Hello, user")
paragraphe.grid(column=0,row=0)

window.mainloop()