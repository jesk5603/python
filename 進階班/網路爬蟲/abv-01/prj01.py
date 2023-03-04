from tkinter import *
import random as r


def hi_fun():
    global clear
    lab.config(text=say[r.randint(0,
                                  len(say) - 1)],
               fg=color[r.randint(0,
                                  len(color) - 1)],
               bg=color[r.randint(0,
                                  len(color) - 1)])


win = Tk()
clear = False
color = [
    "black", "red", "green", "blue", "yellow", "orange", "purple", "pink",
    "brown", "gray"
]
say = ['好痛', 'I am ???', 'you bad']
win.title('My first gui')
btn = Button(win, text=('揍我'), command=hi_fun, fg='#B50061', bg='white')
btn.pack()
lab = Label(win, text='hi', fg='#00BD8A', bg='white')
lab.pack()
win.mainloop()