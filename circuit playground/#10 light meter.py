from adafruit_circuitplayground import cp
import time
import random
cp.pixels.brightness = 0.1

while True:
    x = 30
    while cp.light <= x:
        if cp.light == x:
            for i in range(0, 10-(x//3)):
                cp.pixels[i] = (255,255,255)
            for i in range(9, 10-(x//3),-1):
                cp.pixels[i] = (0,0,0)
        else:
            x -= 3