from tkinter import *

window = Tk()
window.geometry('500x500+500+100')
window.title("Hello my friend")
paragraphe = Label(window, text="Hello, user",font=('Arial bold', 50))
paragraphe.grid(column=0,row=0)
btn = Button(window, text="Click me")
btn.grid(column=0,row=5)

window.mainloop()