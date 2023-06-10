from ttkbootstrap import *
from PIL import Image, ImageTk
import sys
import os
from apple.apple import *
import time

window = tk.Tk()
window.title('Progess Bar Example')


def start_progress():
    for i in range(101):
        progess['value'] = i
        percent_lable.config(text=f'{i}%')
        window.update()
        time.sleep(0.05)


def get_video_info_gui():
    _, _, _, _, res = get_video_info(entry.get())
    res_option['menu'].delete(0, 'end')
    for r in res:
        res_option['menu'].add_command(label=r, command=tk._setit(res_var, r))
    res_var.set(res[0])


def show_Progess(stream, chunk, bytes_remaining):
    percent = (100 * (stream.filesize - bytes_remaining)) / stream.filesize
    percent_lable.config(text=f'{percent:.2f}%')
    progess['value'] = percent
    window.update()


# 定義移動物件的函式，接受一個事件、物件、水平位移和垂直位移
# event: 事件物件為canvas.bind_all要求傳入的參數
def downlaod_video_gui():
    if download_video(entry.get(), res_var.get(), show_Progess):
        lable3.config(text='ok')
    else:
        lable3.config(text='解析度錯誤')


window = tk.Tk()
window.title('Progess Bar Example')

lable = Label(window, text='請輸入youtube影片網址')
lable.grid(row=0, column=0)

lable2 = Label(window, text='請選擇影片解析度')
lable2.grid(row=1, column=0)

lable3 = Label(window, text='下載完成')
lable3.grid(row=2, column=0)

entry = Entry(window)
entry.grid(row=0, column=1)

res_var = tk.StringVar()
res_option = OptionMenu(window, res_var, ())
res_option.grid(row=1, column=1)

but = Button(window,
             text='搜尋影片資訊',
             command=get_video_info_gui,
             style='my.TButton')
but.grid(row=0, column=2)

but1 = Button(window,
              text='下載影片',
              command=downlaod_video_gui,
              style='my.TButton')
but1.grid(row=1, column=2)

# 建立元件
progess = Progressbar(window,
                      orient=HORIZONTAL,
                      length=200,
                      mode='determinate')
progess.grid(row=2, column=1, padx=10, pady=10)
percent_lable = Label(window, text='')
percent_lable.grid(row=2, column=2, padx=10, pady=10)

window.mainloop()