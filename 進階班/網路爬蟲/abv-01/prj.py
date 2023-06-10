# import modules
from ttkbootstrap import *
import os
import time


# user define function
def shutdown():
    for i in range(101):
        progess['value'] = i
        percent_lable.config(text=f'{i}%')
        master.update()
        time.sleep(0.05)
    return os.system("shutdown /s /t 0")


# tkinter object

master = tk.Tk()

progess = Progressbar(master,
                      orient=HORIZONTAL,
                      length=200,
                      mode='determinate')
progess.grid(row=1, column=0)

lable = Label(master, text='hellow')
lable.grid(row=0, column=0, sticky='w')
percent_lable = Label(master, text='')
percent_lable.grid(row=0, column=1, padx=10, pady=10)
can = Canvas(master, width=900, height=900, bg='white')
can.grid()

# creating a button using the widget
# Buttons that will call the submit function
Button(master, text="start", command=shutdown).grid(row=0,
                                                    column=0,
                                                    columnspan=2)

tk.mainloop()