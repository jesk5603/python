from ttkbootstrap import *
from tkinter import filedialog
from PIL import Image, ImageTk
import sys
import os


def open_file():
    global file_path
    file_path = filedialog.askopenfilename(initialdir=sys.path[0])
    lable2.config(text=file_path)  # 顯示檔名


def show_image():
    global file_path
    image = Image.open(file_path)
    image = image.resize((canvas.winfo_width(), canvas.winfo_height()),
                         Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor='nw', image=photo)
    canvas.image = photo


# 定義移動物件的函式，接受一個事件、物件、水平位移和垂直位移
# event: 事件物件為canvas.bind_all要求傳入的參數
def move_object(event, object, dx, dy):
    canvas.move(object, dx, dy)


os.chdir(sys.path[0])
# 創建主視窗
win = tk.Tk()

#設定主視窗標題
win.title('gui')
win.option_add('*font', ('Helvetica', 20))  # 設定預設字型

style = Style(theme='morph')  # 設定主題
style.configure('my.TButton', font=('Helvetica', 20))  # 設定按鈕字型

lable = Label(win, text='選擇檔案:')
lable.grid(row=0, column=0, sticky='E')

but = Button(win, text='瀏覽', command=open_file, style='my.TButton')
but.grid(row=0, column=2, sticky='W')
lable2 = Label(win, text='無')
lable2.grid(row=0, column=1, sticky='E')
but1 = Button(win, text='顯示', command=show_image, style='my.TButton')
but1.grid(row=1, column=0, columnspan=3)
canvas = Canvas(win, width=600, height=600)
canvas.grid(row=2, column=0, columnspan=3)

# a = Button(win, text="揍我", command=u)
# a.grid()
# circle = can.create_oval(300, 300, 500, 400, fill='red')
# img = PhotoImage(file='')
# image = Image.open('image_processing20200510-6203-zo6e7m.png')
# img = ImageTk.PhotoImage(image)
# my_img = can.create_image(400, 400, image=img)
# msg = can.create_text(400, 350, text='++++', fill='black', font=('Arial', 30))

#開始執行主迴圈
# 將按鍵事件綁定到畫布上，當按下指定的按鍵時，移動對應的物件
# can.bind_all('<Right>', lambda event: move_object(event, circle, 10, 0))
# can.bind_all('<Left>', lambda event: move_object(event, circle, -10, 0))
# can.bind_all('<Up>', lambda event: move_object(event, circle, 0, -10))
# can.bind_all('<Down>', lambda event: move_object(event, circle, 0, 10))
# can.bind_all('<d>', lambda event: move_object(event, msg, 10, 0))
# can.bind_all('<a>', lambda event: move_object(event, msg, -10, 0))
# can.bind_all('<w>', lambda event: move_object(event, msg, 0, -10))
# can.bind_all('<s>', lambda event: move_object(event, msg, 0, 10))
win.mainloop()