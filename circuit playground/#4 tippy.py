from adafruit_circuitplayground import cp
import time
import random
cp.pixels.brightness = 0.1

while True:
    cp.pixels.fill((0,0,0))
    x,y,z = cp.acceleration
    if x <= 0: 
        for i in range(6,9):
            cp.pixels[i] = (255,0,0)
    elif x > 0: 
        for i in range(1,4):
            cp.pixels[i] = (0,255,0)