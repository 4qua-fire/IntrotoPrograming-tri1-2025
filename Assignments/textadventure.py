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
    elif exit == "wake up":      #secret option
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
    path = input("Current options:\n1. Continue onward\n2. turn around\n3. leave path\n>")
    if path == "1":
        event_loop()
    elif path == "2": 
        text_strait_turnaround()
    elif path == "3":
        event_moon()
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
    global var_loop_count
    dashes()
    print("The path seems to strech endlessly")
    loop_path = input("Current options:\n1. Continue forward\n2. Turn around\n3. Leave path\n>")
    if loop_path == "1":
        var_loop_count+= 1
        event_loop()
    elif loop_path == "2":
        var_loop_count += 1
        event_loop()
    elif loop_path == "3":
        event_moon()
    else:
        error()
        event_loop()

def event_moon():
    dashes()
    print("The moon shines brightly through the trees\nFollowing the path of least resistance you find yourself at a juction")
    moon_path = input("Current options:\n1. take the left path\n2. take the right path\n>")
    if moon_path == "1":
        dashes()
        print("RETURN ACTIVATED")
        print(" - "*17)
        event_chase()
    if moon_path == "2":
        print("right")
    if moon_path == "3":        #secret option
        print("death")

    
def event_chase():
    print("it seems left was the wrong choice\ntowering over you is a face with yellow eyes and teeth")
    chase_action = input("what are you going to do\n>")

    if len(chase_action) > 10:
        half_dash()
        print("You were to slow to react\nbefore you knew it everything went black\n\n[Hint: Try entering a shorter message]\n")
        replay = input("choose an option to continue\n1. Try again from return\n2. Restart story\n>")
        if replay == "1":
            dashes()
            event_chase()
        if replay == "2":
            print("\n"*10)
            event_start()
   
    elif "run" in chase_action or "flee" in chase_action or "bolt" in chase_action:
        print("run away")
    
    elif "fight" in chase_action or "attack" in chase_action:
        print("fight")
    
    else:
        print("In fear of the monster you couldn't think clearly and it killed you\n\n[Hint: Try entering a simple and relevant action]\n")
        replay = input("choose an option to continue\n1. Try again from return\n2. Restart story\n>")
        if replay == "1":
            dashes()
            event_chase()
        if replay == "2":
            print("\n"*10)
            event_start()
   
    


if len("run away") == 8:
    print("run away")


event_start()
