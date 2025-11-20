from adafruit_circuitplayground import cp
import time
import random
cp.pixels.brightness = 0.1

code = ["A", "A", "B", "A", "B", "B", "B", "A", "A+B"]
attempt = []
presses = 0
while True:
    time.sleep(0.25)   
    if cp.button_a and cp.button_b:
        attempt.append("A+B")
        presses +=1
    elif cp.button_a:
        attempt.append("A")
        presses+= 1
    elif cp.button_b:
        attempt.append("B")
        presses+= 1
    if len(attempt) == len(code):
        if attempt == code:
            for i in range(5):
                cp.pixels.fill((0,255,0))
                cp.play_tone(800, 0.5)
                cp.pixels.fill((0,0,0))
        else:
            for i in range(5):
                cp.pixels.fill((255,0,0))
                cp.play_tone(500, 0.5)
                cp.pixels.fill((0,0,0))
        attempt = []
        presses = 0 
    for i in range(presses%10):
        cp.pixels[i] = (0,0,255)