import mcu
from machine import Pin, I2C
import ssd1306
from umqtt.simple import MQTTClient
import time


def on_message(topic, msg):
    global m
    msg = msg.decode("utf-8")  # Byte to str
    topic = topic.decode("utf-8")
    print(f"my subscribe topic:{topic}, msg:{msg}")
    m = msg


wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"IP={wi.ip}")


mqtt = mcu.MQTT("hello", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234")


mqtt.connet()
mqtt.subscribe("hello", on_message)
m = ""

gpio = mcu.gpio()
i2c = I2C(scl=Pin(gpio.D1), sda=Pin(gpio.D2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    # 查看是否有訂閱主題發布的資料
    mqtt.check_msg()
    oled.fill(0)
    oled.text(f"{wi.ip}", 0, 0)
    oled.text("hello", 0, 10)
    oled.text(f"{m}", 0, 20)
    oled.show()
    time.sleep(0.1)
