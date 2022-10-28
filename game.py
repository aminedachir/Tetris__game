from multiprocessing.connection import wait
from tkinter import *
import time

T = ['red','blue','green']
for i in range(3):
    window = Tk()
    window.config(background=T[i])
    time.sleep(5)
    window.destroy()

window.mainloop()