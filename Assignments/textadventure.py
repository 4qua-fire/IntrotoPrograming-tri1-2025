#general functions
def dashes():   
    print("\n"+"-"*50)
def option_error():
    print("Error: not an option\nPlease type the number of the choice you would like")


def event_start():
    dashes()
    print("You wake up in a cave\nYou dont know where you are\n")
    exit = input("Current options:\n1. Stay in the cave\n2. Leave the cave\n>")
    
    if exit == "1":
        print("event_stay()")
    elif exit == "2":
        event_leave()
    elif exit == "wake up":
        print("awake_death()")
    else:
        option_error()

def event_cave_return():
    dashes()
    print("You returned to the cave\n")
    exit = input("Current options:\n1. Stay in the cave\n2. Leave the cave\n>")
    
    if exit == "1":
        print("event_stay()")
    elif exit == "2":
        event_leave()
    else:
        print("Error: not an option\nPlease type the number of the choice you would like")


def event_leave():
    dashes()
    print("You leave the cave\nYou see that you are in a clearing in a forest")
    clearing = input("Current options:\n1. return to the cave\n2. continue into the trees\n 3.investigate the trees\n>")
    if clearing == "1":
        print(event_cave_return())
    elif clearing == "2":
        print("into_trees()")
    elif clearing == "3":
        print("investigate_trees")
    else:
        option_error()
event_start()
