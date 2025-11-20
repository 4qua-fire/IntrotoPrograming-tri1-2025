from adafruit_circuitplayground import cp
import time
import random
cp.pixels.brightness = 0.1

while True:
    if cp.button_a:
        cp.pixels.fill((0,0,0))
        x = random.randint(0,10)
        for i in range(x):
            if x == 0:
                cp.pixels.fill((0,0,0))
            cp.pixels[i] = (0,255,0)
        time.sleep(0.25)