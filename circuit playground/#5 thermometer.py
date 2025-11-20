from adafruit_circuitplayground import cp
import time
import random
cp.pixels.brightness = 0.1

while True:
    x = cp.temperature
    temp = ( x* 9 / 5) + 32
    cp.pixels[0] = (0, 0, 255)
    if temp> 78:
        cp.pixels[1] = (0, 0, 255)
    if temp> 79:
        cp.pixels[2] = (0, 0, 255)
    if temp> 80:
        cp.pixels[3] = (255, 255, 0)
    if temp> 81:
        cp.pixels[4] = (255, 255, 0)
    if temp> 82:
        cp.pixels[5] = (255, 255, 0)
    if temp> 83:
        cp.pixels[6] = (255, 255, 0)
    if temp> 84:
        cp.pixels[7] = (255, 0, 0)
    if temp> 85:
        cp.pixels[8] = (255, 0, 0)
    if temp> 86:
        cp.pixels[9] = (255, 0, 0)