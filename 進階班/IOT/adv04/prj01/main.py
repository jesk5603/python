#########################匯入模組#########################
from machine import Pin, ADC
from time import sleep
import mcu

#########################函式與類別定義#########################


#########################宣告與設定#########################
gpio = mcu.gpio()
light_sensor = ADC(0)  # 建立 ADC 物件
RED = Pin(gpio.D5, Pin.OUT)
GREEN = Pin(gpio.D6, Pin.OUT)
BLUE = Pin(gpio.D7, Pin.OUT)

RED.value(0)
BLUE.value(0)
GREEN.value(0)

#########################主程式#########################
while True:
    light_sensor_reading = light_sensor.read()  # 讀取類比數位轉換器輸出
    print(
        f"value={light_sensor_reading}, {round(light_sensor_reading * 100 / 1024)}%"
    )  # 顯示值
    sleep(1)  # 延遲 1 秒

    if light_sensor_reading > 700:
        GREEN.value(1)
    else:
        GREEN.value(0)
