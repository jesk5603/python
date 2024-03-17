#########################匯入模組#########################
from machine import Pin, PWM
from time import sleep
import mcu

#########################函式與類別定義#########################

#########################宣告與設定#########################
gpio = mcu.gpio()
# RED = Pin(gpio.D5, Pin.OUT)
# GREEN = Pin(gpio.D6, Pin.OUT)
# BLUE = Pin(gpio.D7, Pin.OUT)
frequency = 1000
duty_cycle = 0
RED = PWM(Pin(gpio.D5), freq=frequency, duty=duty_cycle)
GREEN = PWM(Pin(gpio.D6), freq=frequency, duty=duty_cycle)
BLUE = PWM(Pin(gpio.D7), freq=frequency, duty=duty_cycle)
a = 0
b = 0
c = 1023
while True:
    while a != 1023:
        BLUE.duty(c)
        sleep(0.0005)
        c -= 1
        RED.duty(a)
        sleep(0.0005)
        a += 1
    while b != 1023:
        RED.duty(a)
        sleep(0.0005)
        a -= 1
        GREEN.duty(b)
        sleep(0.0005)
        b += 1
    while c != 1023:
        GREEN.duty(b)
        sleep(0.0005)
        b -= 1
        BLUE.duty(c)
        sleep(0.0005)
        c += 1
