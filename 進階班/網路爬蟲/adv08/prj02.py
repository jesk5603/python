from ttkbootstrap import *
from PIL import Image, ImageTk
import os
import sys
import requests
from matplotlib.font_manager import FontProperties
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import datetime

os.chdir(sys.path[0])

api_key = "892da2f13edf3c7f382637760e72d224"  # API Key
base_url = "https://api.openweathermap.org/data/2.5/onecall?"  # API URL
lon = '121.5319'
lat = '25.0478'
exclude = 'minutely,hourly'
units = "metric"  # 單位 (公制)
lang = "zh_tw"  # 語言 (繁體中文)


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

    send_url = base_url
    send_url += 'lat=' + lat_entry.get()
    send_url += '&lon=' + lon_entry.get()
    send_url += '&exclude=' + exclude
    send_url += '&appid=' + api_key
    send_url += '&units=' + units
    send_url += '&lang=' + lang

    print(send_url)  # 印出發送的 URL

    response = requests.get(send_url)
    info = response.json()

    if 'daily' in info.keys():
        global temp

        icon_code = info['current']['weather'][0]['icon']
        icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
        response = requests.get(icon_url)
        with open(f'{icon_code}.png', 'wb') as icon_file:
            icon_file.write(response.content)

        check_label4.config(
            text=f"描述:{info['current']['weather'][0]['description']}")
        check_label3.config(text=f"溫度={info['current']['temp']}")
        check_label.config(text=f"目前搜尋的地區:{info['timezone']}")
        temp = info['current']['temp']
        image = Image.open(f'{icon_code}.png')
        tk_image = ImageTk.PhotoImage(image)
        check_label2.config(image=tk_image)
        check_label2.image = tk_image

        listX = []
        listY = []
        for i in range(7):
            temp = info['daily'][i]['temp']['day']
            time = datetime.datetime.fromtimestamp(
                info['daily'][i]['dt']).strftime('%m/%d')
            print(f'{time}的溼度是{temp}度')
            listX.append(time)
            listY.append(temp)

        font = FontProperties(fname='TaipeiSansTCBeta-Bold.ttf', size=14)
        fig, ax = plt.subplots()
        ax.plot(listX, listY)
        ax.set_xlabel('日期', fontproperties=font)
        ax.set_ylabel('溫度', fontproperties=font)
        ax.set_title('七天氣象預測', fontproperties=font)

        canvas = FigureCanvasTkAgg(fig, master=win)
        canvas.draw()  # 繪製圖形
        canvas = canvas.get_tk_widget()
        canvas.grid(row=4, column=1, columnspan=3, padx=10, pady=10)
    else:
        check_label.config(text="目前搜尋的地區:找不到該城市")


win = tk.Tk()
win.option_add('*font', ('Helvetica', 20))  # 設定預設字型
style = Style(theme='morph')  # 設定主題
style.configure('my.TButton', font=('Helvetica', 20))  # 設定按鈕字型
style.configure('my.TCheckbutton', font=('Helvetica', 20))  # 設定按鈕字型

check_label = Label(win, text='目前搜尋的地區:?')
check_label.grid(row=0, rowspan=2, column=1)

check_button = Button(win, text='獲得天氣資訊', command=weather, style='my.TButton')
check_button.grid(row=0, rowspan=2, column=3)

lon_var = StringVar()
lon_var.set(lon)
lon_entry = Entry(win, width=20, textvariable=lon_var)
lon_entry.grid(row=0, column=2, padx=10, pady=10)

lat_var = StringVar()
lat_var.set(lat)
lat_entry = Entry(win, width=20, textvariable=lat_var)
lat_entry.grid(row=1, column=2, padx=10, pady=10)

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
