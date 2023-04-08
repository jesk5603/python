from ttkbootstrap import *
from tkinter import filedialog
from PIL import Image, ImageTk
import sys
import os

win = tk.Tk()
win.title('機算機')
win.option_add('*font', ('Helvetica', 20))  # 設定預設字型


def test():
    entry_text = entry.get()
    try:
        ans = eval(entry_text)
    except:
        ans = 'error'
    label.config(text=ans)


style = Style(theme='morph')  # 設定主題
style.configure('my.TButton', font=('Helvetica', 20))  # 設定按鈕字型
entry = Entry(win, width=30)
entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
but = Button(win, text='顯示計算結果', command=test, style='my.TButton')
but.grid(row=1, column=0, columnspan=2, sticky='WE', padx=10, pady=10)
label = Label(win, text='計算結果')
label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
win.mainloop()