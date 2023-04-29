from ttkbootstrap import *
from PIL import Image, ImageTk
import os
import sys
import requests

api_key = 'bd06d5a9b81122200eb8325256559234'
base_url = 'https://api.openweathermap.org/data/2.5/weather?'

os.chdir(sys.path[0])


def on_switch_change():
    global units, temp
    if check_type.get():
        units = 'metric'
    else:
        units = 'imperial'

    if check_label3.cget('text') != '溫度:?〫C':

        if units == 'metric':
            temp = round(5 / 9 * (temp - 32), 2)
            check_label3.config(text=f"溫度={temp}C")
        else:
            temp = round((temp * 9 / 5) + 32, 2)
            check_label3.config(text=f"溫度={temp}F")


def weather():
    global units
    city_name = check_entry.get()  #輸入城市名稱
    units = 'metric'  #單位
    lang = 'zh_tw'  #語言
    send_url = base_url
    send_url += 'appid=' + api_key
    send_url += '&q=' + city_name
    send_url += '&units=' + units
    send_url += '&lang=' + lang
    response = requests.get(send_url)
    info = response.json()
    # print(f"city={info['name']}")
    # print(f"溫度={info['main']['temp']}")
    # print(f"描述={info['weather'][0]['description']}")
    if 'main' in info.keys():
        global temp
        icon_code = info['weather'][0]['icon']
        icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
        response = requests.get(icon_url)
        with open(f'{icon_code}.png', 'wb') as icon_file:
            icon_file.write(response.content)

        check_label4.config(text=f"描述:{info['weather'][0]['description']}")
        check_label3.config(text=f"溫度={info['main']['temp']}")
        temp = info['main']['temp']
        image = Image.open(f'{icon_code}.png')
        tk_image = ImageTk.PhotoImage(image)
        check_label2.config(image=tk_image)
        check_label2.image = tk_image
    else:
        print('City Not Found')


win = tk.Tk()
win.option_add('*font', ('Helvetica', 20))  # 設定預設字型
style = Style(theme='morph')  # 設定主題
style.configure('my.TButton', font=('Helvetica', 20))  # 設定按鈕字型
style.configure('my.TCheckbutton', font=('Helvetica', 20))  # 設定按鈕字型

check_label = Label(win, text='請輸入想搜尋的城市:')
check_label.grid(row=1, column=1)

check_button = Button(win, text='獲得天氣資訊', command=weather, style='my.TButton')
check_button.grid(row=1, column=3)

check_entry = Entry(win)
check_entry.grid(row=1, column=2)

check_label2 = Label(win, text='天氣圖標')
check_label2.grid(row=2, column=1)

check_label3 = Label(win, text='溫度:?度C')
check_label3.grid(row=2, column=2)

check_label4 = Label(win, text='描述:?')
check_label4.grid(row=2, column=3)

check_type = BooleanVar()

check_type.set(True)

check = Checkbutton(win,
                    text='溫度單位(C/F)',
                    style="my.TCheckbutton",
                    variable=check_type,
                    onvalue=True,
                    offvalue=False,
                    command=on_switch_change)
check.grid(row=3, column=2)
win.mainloop()
