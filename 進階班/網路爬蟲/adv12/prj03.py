from ttkbootstrap import *
from PIL import Image, ImageTk
import sys
import os
from apple.apple import *


def get_video_info_gui():
    _, _, _, _, res = get_video_info(entry.get())
    res_option['menu'].delete(0, 'end')
    for r in res:
        res_option['menu'].add_command(label=r, command=tk._setit(res_var, r))
    res_var.set(res[0])


# 定義移動物件的函式，接受一個事件、物件、水平位移和垂直位移
# event: 事件物件為canvas.bind_all要求傳入的參數
def downlaod_video_gui():
    if download_video(entry.get(), res_var.get()):
        lable3.config(text='ok')
    else:
        lable3.config(text='解析度錯誤')


os.chdir(sys.path[0])
# 創建主視窗
win = tk.Tk()

#設定主視窗標題
win.title('gui')
win.option_add('*font', ('Helvetica', 20))  # 設定預設字型

style = Style(theme='morph')  # 設定主題
style.configure('my.TButton', font=('Helvetica', 20))  # 設定按鈕字型

lable = Label(win, text='請輸入youtube影片網址')
lable.grid(row=0, column=0)

lable2 = Label(win, text='請選擇影片解析度')
lable2.grid(row=1, column=0)

lable3 = Label(win, text='下載完成')
lable3.grid(row=2, column=0)

entry = Entry(win)
entry.grid(row=0, column=1)

res_var = tk.StringVar()
res_option = OptionMenu(win, res_var, ())
res_option.grid(row=1, column=1)

but = Button(win,
             text='搜尋影片資訊',
             command=get_video_info_gui,
             style='my.TButton')
but.grid(row=0, column=2)

but1 = Button(win, text='下載影片', command=downlaod_video_gui, style='my.TButton')
but1.grid(row=1, column=2)

win.mainloop()
