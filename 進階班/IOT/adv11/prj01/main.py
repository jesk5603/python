from machine import Pin, PWM
import mcu
import time


gpio = mcu.gpio()
servo = mcu.servo(gpio.D8)

while True:
    servo.angle(90)
    time.sleep(1)
    servo.angle(180)
    time.sleep(1)
    servo.angle(90)
    time.sleep(1)
    servo.angle(0)
    time.sleep(1)
