from tkinter import *

from setuptools import Command

window = Tk()
window.title("facebook")
window.geometry("500x650+500+50")

def Click():
    paragraphe.configure(text="   ")
    facebook.configure(text="    ")
    user_mail.configure(width=0)
    user_password.configure(width=0)
    login = Label(window,text="Log in Suuccefuly")
    login.grid(row=0,column=0)

paragraphe = Label(window, text="       ")
facebook = Label(window, text="Facebook", fg="Blue", font=('Arial bold', 45))

paragraphe.grid(padx=0, pady=80)
facebook.grid(padx=115, pady=10)

user_mail = Entry(window,width=35)
user_password = Entry(window,width=35)

user_mail.grid(pady=10)
user_password.grid(padx=15,pady=10)

btn = Button(window,text="Log in",width=9,fg='white',bg='blue',command=Click)
btn.grid(padx=115,pady=10)


window.mainloop()