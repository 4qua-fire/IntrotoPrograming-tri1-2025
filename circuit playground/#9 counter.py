from adafruit_circuitplayground import cp
import time
import random
cp.pixels.brightness = 0.1

count = 0
while True:
    if cp.button_a and count < 10:
        count += 1
        time.sleep(0.25)
    if cp.button_b and count >= 0:
        count -= 1
        time.sleep(0.25)
        cp.pixels.fill((0,0,0))
    for i in range(count):
        cp.pixels[i]=((255,0,0))