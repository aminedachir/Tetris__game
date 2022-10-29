from multiprocessing.connection import wait
from tkinter import *
import time

T = ['red','blue','green']
for i in range(3):
    window = Tk()
    window.config(background=T[i])

C = ["50", "100", "200"]
for i in range(3):
    window = Tk()
    time.sleep(1)
    txt = Label(window,text="AMINE")
    txt.place(x=C[i],y=C[i])

window = Tk()
M = ['iconic', 'normal']
for i in range(2):
    window.state(M[i])
    time.sleep(1)

window.mainloop()