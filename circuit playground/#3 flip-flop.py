from adafruit_circuitplayground import cp
import time
import random
cp.pixels.brightness = 0.1

prev_switch = cp.switch #so it doesnt blink
while True:
    if prev_switch != cp.switch:
        cp.pixels.fill((0,0,0))
    prev_switch = cp.switch
    if cp.switch:
        for i in range(5):
            cp.pixels[i] = (0,255,0)
    else: 
        for i in range(5,10):
            cp.pixels[i] = (0,255,0)