#########################匯入模組#########################
from time import sleep
from machine import Pin, ADC, PWM
import mcu


#########################函式與類別定義#########################

#########################宣告與設定#########################
frequency = 1000
duty_cycle = 0

gpio = mcu.gpio()
light_sensor = ADC(0)  # 建立 ADC 物件
RED = PWM(Pin(gpio.D5), freq=frequency, duty=duty_cycle)
GREEN = PWM(Pin(gpio.D6), freq=frequency, duty=duty_cycle)
BLUE = PWM(Pin(gpio.D7), freq=frequency, duty=duty_cycle)

#########################主程式#########################
while True:
    duty_cycle = light_sensor.read()  # 讀取類比數位轉換器輸出
    print(duty_cycle)
    sleep(0.5)  # 延遲 1 秒

    if duty_cycle < 600:
        duty_cycle = 0

    RED.duty(duty_cycle)
    GREEN.duty(duty_cycle)
    BLUE.duty(duty_cycle)
