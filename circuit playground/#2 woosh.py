from adafruit_circuitplayground import cp
import time
import random
cp.pixels.brightness = 0.1

while True:
    if cp.button_a:
        for i in range(10):
            cp.pixels[i] = (0,0,255)
            time.sleep(0.1)
            cp.pixels[i] = (0,0,0)