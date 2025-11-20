from adafruit_circuitplayground import cp
import time
import random
cp.pixels.brightness = 0.1

color = 0
while True:
    if cp.button_a:
        color += 1
        time.sleep(0.25)
    if color%7 == 0:
        cp.pixels.fill((255,0,0))
    elif color%7 == 1:
        cp.pixels.fill((255,80,0))
    elif color%7 == 2:
        cp.pixels.fill((200,200,0))
    elif color%7 == 3:
        cp.pixels.fill((0,255,0))
    elif color%7 == 4:
        cp.pixels.fill((0,0,255))
    elif color%7 == 5:
        cp.pixels.fill((128,0,255))
    elif color%7 == 6:
        cp.pixels.fill((255,80,255))