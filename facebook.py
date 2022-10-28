from tkinter import *

window = Tk()
window.title("facebook")
window.geometry("500x650+500+50")
paragraphe = Label(window, text="       ", fg="Blue", font=('Arial bold', 45))
paragraphe.grid(column=10, row=0)
paragraphe = Label(window, text="Facebook", fg="Blue", font=('Arial bold', 45))
paragraphe.grid(column=15, row=2)

window.mainloop()