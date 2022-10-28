from multiprocessing.connection import wait
from tkinter import *

T = ['red','blue','green']
for i in range(3):
    window = Tk()
    window.config(background=T[i])

window.mainloop()