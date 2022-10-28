from tkinter import *

window = Tk()
window.title("facebook")
window.geometry("500x650+500+50")

def Click():
    locx, locy = btn.winfo_x(), btn.winfo_y()
    btn.place(x=-locx,y=-locy)
    facebook.place(x=-locx,y=-locy)
    user_mail.place(x=-locx,y=-locy)
    user_password.place(x=-locx,y=-locy)
    mail.place(x=-locx,y=-locy)
    password.place(x=-locx,y=-locy)
    text_message = Label(window,text="Logged in Succefuly",font=('Arial bold', 30))
    text_message.place(x=85,y=280)

facebook = Label(window, text="Facebook", fg="Blue", font=('Arial bold', 45))

facebook.place(x=125, y=180)

mail = Label(window,text="Address email : ")
password = Label(window,text="Password : ")

mail.place(x=65,y=270)
password.place(x=65,y=300)

user_mail = Entry(window,width=35)
user_password = Entry(window,width=35)

user_mail.place(x=150,y=270)
user_password.place(x=150,y=300)

btn = Button(window,text="Log in",width=9,fg='white',bg='blue',command=Click)
btn.place(x=225,y=340)

window.mainloop()