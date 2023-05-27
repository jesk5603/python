import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ttkbootstrap import *
import requests  # 載入 requests 套件 (用來發送請求) 內建json模組
import datetime
import os
import sys
from matplotlib.font_manager import FontProperties

os.chdir(sys.path[0])


def draw_graph():
    api_key = "892da2f13edf3c7f382637760e72d224"  # API Key
    base_url = "https://api.openweathermap.org/data/2.5/onecall?"  # API URL
    lon = '121.5319'
    lat = '25.0478'
    exclude = 'minutely,hourly'
    units = "metric"  # 單位 (公制)
    lang = "zh_tw"  # 語言 (繁體中文)

    send_url = base_url
    send_url += 'lat=' + lat
    send_url += '&lon=' + lon
    send_url += '&exclude=' + exclude
    send_url += '&appid=' + api_key
    send_url += '&units=' + units
    send_url += '&lang=' + lang

    print(send_url)  # 印出發送的 URL

    response = requests.get(send_url)
    info = response.json()

    listX = []
    listY = []
    if 'daily' in info.keys():
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

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()  # 繪製圖形
        canvas = canvas.get_tk_widget()
        canvas.grid(row=0, column=0, padx=10, pady=10)
    else:
        print('Request Fail')


def on_closing():
    window.destroy()
    plt.close('all')


window = tk.Tk()
window.protocol("WM_DELETE_WINDOW", on_closing)
style = Style(theme="minty")
draw_button = Button(window, text="Draw Graph", command=draw_graph)
draw_button.grid(row=1, column=0, padx=10, pady=10)
window.mainloop()