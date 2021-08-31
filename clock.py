from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Edo's Clock")

def time():
    string =strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)

label = Label(root,font=('Bahnschrift SemiBold',80),background='black',foreground='yellow')
label.pack(anchor='center')
time()
mainloop()


#learned from https://www.youtube.com/watch?v=at7rpdT8FeI