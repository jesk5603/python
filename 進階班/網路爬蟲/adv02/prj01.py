from tkinter import *
import sys
import os


def u():
    win.destroy()


# 定義移動物件的函式，接受一個事件、物件、水平位移和垂直位移
# event: 事件物件為canvas.bind_all要求傳入的參數
def move_object(event, object, dx, dy):
    can.move(object, dx, dy)


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

#開始執行主迴圈
# 將按鍵事件綁定到畫布上，當按下指定的按鍵時，移動對應的物件
can.bind_all('<Right>', lambda event: move_object(event, circle, 10, 0))
can.bind_all('<Left>', lambda event: move_object(event, circle, -10, 0))
can.bind_all('<Up>', lambda event: move_object(event, circle, 0, -10))
can.bind_all('<Down>', lambda event: move_object(event, circle, 0, 10))
can.bind_all('<d>', lambda event: move_object(event, msg, 10, 0))
can.bind_all('<a>', lambda event: move_object(event, msg, -10, 0))
can.bind_all('<w>', lambda event: move_object(event, msg, 0, -10))
can.bind_all('<s>', lambda event: move_object(event, msg, 0, 10))
win.mainloop()
