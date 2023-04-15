import requests
import os
import sys

os.chdir(sys.path[0])

api_key = 'bd06d5a9b81122200eb8325256559234'
base_url = 'https://api.openweathermap.org/data/2.5/weather?'
city_name = input('Enter city name')  #輸入城市名稱
units = 'metric'  #單位
lang = 'zh_tw'  #語言
send_url = base_url
send_url += 'appid=' + api_key
send_url += '&q=' + city_name
send_url += '&units=' + units
send_url += '&lang=' + lang
response = requests.get(send_url)
info = response.json()
print(f"city={info['name']}")
print(f"溫度={info['main']['temp']}")
print(f"描述={info['weather'][0]['description']}")
if 'main' in info.keys():
    icon_code = info['weather'][0]['icon']
    icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
    response = requests.get(icon_url)
    with open(f'{icon_code}.png', 'wb') as icon_file:
        icon_file.write(response.content)
else:
    print('City Not Found')
