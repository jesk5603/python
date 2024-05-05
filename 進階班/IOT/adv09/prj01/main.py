import mcu
from machine import Pin, I2C
import ssd1306


####宣告宇設定
gpio = mcu.gpio()
i2c = I2C(scl=Pin(gpio.D1), sda=Pin(gpio.D2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)


###主程式
oled.fill(0)  # 清除螢幕
oled.text("Hello", 0, 0)
oled.text("world", 0, 10)
oled.show()
