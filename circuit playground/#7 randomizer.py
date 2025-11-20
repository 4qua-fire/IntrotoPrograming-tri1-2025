from adafruit_circuitplayground import cp
import time
import random
cp.pixels.brightness = 0.1

while True:
    x, y, z = cp.acceleration
    if abs(x) > 15 or abs(y) > 15 or abs(z) > 15:
        for i in range(10):
            a = random.randint(0,255)*random.randint(0,1)
            b = random.randint(0,255)*random.randint(0,1)
            c =  random.randint(0,255)*random.randint(0,1)
            cp.pixels[i] =(a,b,c)
