from adafruit_circuitplayground import cp
import time
import random
cp.pixels.brightness = 0.1

while True:
    cp.pixels.fill((0,255,0))
    time.sleep(.367)
    cp.pixels.fill((0,0,0))
    time.sleep(.367)