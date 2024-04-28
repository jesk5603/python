#########################匯入模組#########################

import time
import mcu
from machine import Pin, ADC
from mcu import MQTT


#########################函式與類別定義#########################
def on_message(topic, msg):
    global m
    msg = msg.decode("utf-8")  # Byte to str
    topic = topic.decode("utf-8")
    print(f"my subscribe topic:{topic}, msg:{msg}")
    m = msg


def LED_ON():
    LED.RED.value(1)
    LED.GREEN.value(1)
    LED.BLUE.value(1)


def LED_OFF():
    LED.RED.value(0)
    LED.GREEN.value(0)
    LED.BLUE.value(0)


#########################宣告與設定#########################
wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"IP={wi.ip}")


mqtt = mcu.MQTT(
    "stephen", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234"
)

mqtt.connet()


mqtt.subscribe("hello", on_message)


gpio = mcu.gpio()
LED = mcu.LED(gpio.D5, gpio.D6, gpio.D7, pwm=False)


LED.RED.value(0)
LED.GREEN.value(0)
LED.BLUE.value(0)
light_sensor = ADC(0)  # 建立 ADC 物件
m = ""
#########################主程式#########################
while True:
    # 查看是否有訂閱主題發布的資料
    mqtt.check_msg()

    light_sensor_reading = light_sensor.read()  # 讀取類比數位轉換器輸出
    if m == "on":
        LED_ON()
    elif m == "off":
        LED_OFF()
    elif m == "auto":
        if light_sensor_reading > 700:
            LED_ON()
        else:
            LED_OFF()
    time.sleep(0.1)
