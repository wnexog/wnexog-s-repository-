import time
from tkinter import *

window = Tk()
button = Button(window, text="Start/ Stop")


state = {'active': False, 'start_time': None}


def tick():
    if state['active']:
        end_time = time.time()
        x = float(end_time - state['start_time'])
        y = str(round(4.905 * x ** 2, 2))
        z = str(round((float(y)) * 3.28, 2))
        x = str(round(x, 2))
        print("Time fallen= " + x + " seconds" + " Height= " + y + " meters" " Height= " + z + " feet \n")
        window.after(100, tick)


def timer_f():
    state['active'] = not state['active']
    if state['active']:
        state['start_time'] = time.time()
        tick()


button.config(command=timer_f)  # performs callback of function
button.config(font=("Ink Free", 50, "bold"))  # changes font
button.config(bg="#32a2a8")  # changes background colour of button
button.config(fg="#99a832")
button.config(activebackground="#FF0000")
button.config(activeforeground="#99a832")
button.pack()
window.mainloop()
