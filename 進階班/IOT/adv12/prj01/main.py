from machine import Pin
import mcu
import time

gpio = mcu.gpio()
earthquake = Pin(gpio.D3, Pin.IN)

while True:
    print(earthquake.value())
    if earthquake.value() == 1:
        print("Emergency!")
    time.sleep(1)
