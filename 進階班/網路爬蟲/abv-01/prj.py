# import modules
from ttkbootstrap import *
import os


# user define function
def shutdown():
    return os.system("shutdown /s /t 300")


# tkinter object
master = tk.Tk()
master.option_add('*font', ('Helvetica', 20))
style = Style(theme='vapor')
style.configure('my.TButton', font=('Helvetica', 20))
lable = Label(master, text='hellow')
lable.grid(row=0, column=0, sticky='w')
can = Canvas(master, width=900, height=900, bg='white')
can.grid()

# creating a button using the widget
# Buttons that will call the submit function
Button(master, text="揍我", command=shutdown).grid(row=0)

tk.mainloop()