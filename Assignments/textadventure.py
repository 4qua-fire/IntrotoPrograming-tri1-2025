#variable definition
var_loop_count =0



#repeated functions
def dashes():   
    print("\n"+"-"*51)
def half_dash():
    print("\n"+" - "*17)
def error():
    print("Error: not an option\nPlease type the number of the choice you would like")


def event_start():
    dashes()
    print("You are in a cave\nYou dont know where you are\n")
    exit = input("Current options:\n1. Stay in the cave\n2. Leave the cave\n>")
    
    if exit == "1":
        print("event_stay()")
    elif exit == "2":
        event_leave()
    elif exit == "wake up":
        print("awake_death()")
    else:
        error()
        event_start()

def event_leave():
    dashes()
    print("You leave the cave\nYou see that you are in a clearing in a forest")
    clearing = input("Current options:\n1. return to the cave\n2. continue into the trees\n3. investigate the trees\n>")
    if clearing ==  "1":
        event_start()
    elif clearing == "2":
        event_strait_path()
    elif clearing == "3":
        print("investigate_trees()")
    else:
        error()
        event_leave()

def event_strait_path():
    dashes()
    print("Ahead of you the path seems to continue endlessly\nThe trees mirror eachother on both sides\nYou hear the sound of Trees break behind you")
    path = input("Current options:\n1. Continue onward\n2. turn around\n3.leave path\n>")
    if path == "1":
        print("event_loop()")
    elif path == "2": 
        text_strait_turnaround()
    elif path == "3":
        print("event_moon()")
    else:
        error()
        event_strait_path()

def text_strait_turnaround():
    half_dash()
    print("turning, around you see that the trees behind you have all fallen down\nyou have no way back")
    if input("1. turn around\n>") == "1":
        event_strait_path()
    else:
        error()
        event_strait_path()

def event_loop():
    dashes()
    print("The path seems to strech endlessly")
    loop_path = input("Current options:\n1.Continue forward\n2. Turn around\n3. Leave path")
    if loop_path == "1":
        var_loop_count+= 1
        event_loop()
    elif loop_path == "2":
        var_loop_count += 1
        event_loop()
    elif loop_path == "3":
        pass


    

event_start()
