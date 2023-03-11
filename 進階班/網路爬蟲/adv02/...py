from tkinter import *
import sys
import os

# 設定工作目錄
os.chdir(sys.path[0])


# Key 控制
def move_circle(event):
    key = event.keysym
    print(key)
    if key == "Right":
        canvas.move(circle, 10, 0)
    elif key == "Left":
        canvas.move(circle, -10, 0)
    elif key == "Up":
        canvas.move(circle, 0, -10)
    elif key == "Down":
        canvas.move(circle, 0, 10)
    elif key == "d":
        canvas.move(rect, 10, 0)
    elif key == "a":
        canvas.move(rect, -10, 0)
    elif key == "w":
        canvas.move(rect, 0, -10)
    elif key == "s":
        canvas.move(rect, 0, 10)


# 建立視窗
windows = Tk()
windows.title("My first GUI")
# windows.iconbitmap("20190911奇點創意-LOGO.ico")

# 建立畫布
canvas = Canvas(windows, width=600, height=600)
canvas.pack()

# 載入圖片
# img = PhotoImage(file="crocodile2.gif")
# 建立圖片物件
# my_img = canvas.create_image(300, 300, image=img)

# 畫圓形
circle = canvas.create_oval(250, 150, 300, 200, fill="red")
# 畫矩形
rect = canvas.create_rectangle(220, 400, 340, 430, fill="blue")
# 加入文字
msg = canvas.create_text(300,
                         100,
                         text="Corcodile",
                         fill="black",
                         font=('Arial', 30))

# 綁定事件
canvas.bind_all('<Key>', move_circle)

# 進入主迴圈
windows.mainloop()