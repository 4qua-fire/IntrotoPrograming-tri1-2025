from adafruit_circuitplayground import cp
import time
import random
cp.pixels.brightness = 0.1

while True: 
    x,y,z = cp.acceleration
    if cp.button_a:
        cp.pixels.fill((0,0,0))
        time.sleep(0.25)
        if y < 0 and y > x: 
            for i in range(1,5):
                cp.pixels[round(((1/6)*(i**3))+(-1.5*(i**2))+((16/3)*i)-2)] = (200,200,0)
        if y > 0 and y > x: 
            for i in range(1,4):
                cp.pixels[2**i] = (0,0,255)
        if x < 0 and x > y: 
            for i in range(1,7):
                cp.pixels[i if i <= 4 else i+3] = (255,0,0)
        if x > 0 and x > y: 
            for i in range(1,5):
                cp.pixels[round(((-1/6)*(i**3))+((i**2))+((1/6)*i))] = (0,255,0)