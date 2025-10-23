#path 1 variables
var_loop_count =0
chase_monster = False

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
        event_chill()
    if moon_path == "3":       #secret option
        print("death")
    else:
        error()
        event_moon()

    
def event_chase():
    print("it seems left was the wrong choice\ntowering over you is a face with yellow eyes and teeth")
    global chase_monster
    chase_monster = True
    chase_action = input("what are you going to do\n>")

    if len(chase_action) > 10:
        half_dash()
        print("You were to slow to react\nBefore you knew it everything went black\n\n[Hint: Try entering a shorter message]\n")
        replay = input("choose an option to continue\n1. Try again from return\n2. Restart story\n>")
        if replay == "1":
            dashes()
            event_chase()
        elif replay == "2":
            print("\n"*10)
            event_start()
        else:
            error()
            event_chase()
   
    elif "run" in chase_action or "flee" in chase_action or "bolt" in chase_action:
        event_chase_run()
    
    elif "fight" in chase_action or "attack" in chase_action:
        half_dash()
        print("You attempt to fight the monster\nYou did well considering you were empty handed\nHowever it was all for naught\nBefore all fades to black you hear the beast release a wretched scream and thump onto the earth")
        replay = input("choose an option to continue\n1. Try again from return\n2. Restart story\n>")
        if replay == "1":
            dashes()
            event_chase()
        elif replay == "2":
            print("\n"*10)
            event_start()   
        else:
            error()
            event_chase()
    else:
        half_dash()
        print("In fear of the monster you couldn't think clearly and it killed you\n\n[Hint: Try entering a simple and relevant action]\n")
        replay = input("choose an option to continue\n1. Try again from return\n2. Restart story\n>")
        if replay == "1":
            dashes()
            event_chase()
        elif replay == "2":
            print("\n"*10)
            event_start()
        else:
            error()
            event_chase()
   
def event_chase_run():
    dashes()
    print("you run away from the monster\n after some running you approch an intersection")
    runaway_path = input("Current options\n1. Run to the left\n2. Run to the right\n>")
    if runaway_path == "1":
        print()
    if runaway_path == "2":
        half_dash()
        print("you ran to the right forgetting that that was the route you came from\nYou reach the strait path and continue to run\nThe moment you start to slow it seems the monster is immediatly behind you\nEvery thing fades to black")
        replay = input("choose an option to continue\n1. Try again from return\n2. Restart story\n>")
        if replay == "1":
            dashes()
            event_chase()
        elif replay == "2":
            print("\n"*10)
            event_start()
        else:
            error()
            event_chase_run()

def event_chill():
    dashes()
    if chase_monster:
        print("the danger has passed\nBehind you the monster continues running down the other path\nIts shreiks gradually fading behind you")
    else:
        print("It is getting cold now\nA mist forms with each breath")
        chill_action = input("Current options:\n1. Continue onward\n2. attempt to find warmth")
        if chill_action == "1":
            "ending 1"
        elif chill_action == "2":
            event_warmth()
        else:
            error()
            event_chill()

def event_warmth():
    print("You manage to find a blanket ")
event_start()
