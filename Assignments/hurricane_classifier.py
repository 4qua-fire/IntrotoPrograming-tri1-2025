speed = input("What is the speed of the hurricane in mph? (do not include layer)\n>")
try:
    speed = int(speed)
    if speed < 74:
        print("Hurricane is a tropical storm")
    elif speed < 96:
        print("Hurricane is Category 1")
    elif speed < 111:
        print("Hurricane is Category 2")
    elif speed < 130:
        print("Hurricane is Category 3")
    elif speed < 157:
        print("Hurricane is Category 4")
    elif speed >= 157:
        print("Hurricane is Category 5")
except:
    print("Error")