from tkinter import *
import sys
import os


def u():
    win.destroy()


def move_canvas(event):
    key = event.keysym
    print(key)
    if key == 'Right':
        can.move(circle, 10, 0)
    elif key == 'Left':
        can.move(circle, -10, 0)
    elif key == "Up":
        can.move(circle, 0, -10)
    elif key == "Down":
        can.move(circle, 0, 10)
    elif key == "d":
        can.move(msg, 10, 0)
    elif key == "a":
        can.move(msg, -10, 0)
    elif key == "w":
        can.move(msg, 0, -10)
    elif key == "s":
        can.move(msg, 0, 10)


os.chdir(sys.path[0])
# 創建主視窗
win = Tk()

#設定主視窗標題
win.title('gui')
a = Button(win, text="揍我", command=u)
a.pack()
can = Canvas(win, width=900, height=900, bg='white')
can.pack()
circle = can.create_oval(300, 300, 500, 400, fill='red')
img = PhotoImage(file='image_processing20200510-6203-zo6e7m.png')
my_img = can.create_image(400, 400, image=img)
msg = can.create_text(400, 350, text='++++', fill='black', font=('Arial', 30))
can.bind_all('<Key>', move_canvas)
#開始執行主迴圈
win.mainloop()
