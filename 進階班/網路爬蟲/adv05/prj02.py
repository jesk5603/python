from ttkbootstrap import *
import os
import sys

os.chdir(sys.path[0])


def on_switch_change():
    check_label.config(text=str(check_type.get()))


win = tk.Tk()
win.option_add('*font', ('Helvetica', 20))  # 設定預設字型
style = Style(theme='morph')  # 設定主題
style.configure('my.TButton', font=('Helvetica', 20))  # 設定按鈕字型

check_type = BooleanVar()

check_type.set(True)

check_label = Label(win, text='True')
check_label.grid(row=1, column=2)

check = Checkbutton(win,
                    variable=check_type,
                    onvalue=True,
                    offvalue=False,
                    command=on_switch_change)
check.grid(row=1, column=1)
win.mainloop()