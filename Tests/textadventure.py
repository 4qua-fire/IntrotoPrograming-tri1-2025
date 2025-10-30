#imports
import sys
import random
#variables
var_loop_count =0
chase_monster = False
small_unlocked = False
dash_count =0
#repeated functions
def dashes():
	global dash_count
	dash_count += 1
	print(f"\n{dash_count}{"-"*51}")
def half_dash():
	global dash_count
	dash_count += 1
	print(f"\n{dash_count}{" - "*17}")
def error():
    print("Error: not an option\nPlease type the value of the choice you would like")
def ending_dash():
    print("\n"*5)
    print("*"*51)
    print("***************************************************\n")

#start functions
def event_cave():
    global var_loop_count, chase_monster, small_unlocked
    dashes()
    if small_unlocked == True:
        print("You are back in the main room of the cave\n")
        exit = input("\nCurrent Options:\n1. Look around the main room\n2. Look around the small room\n3. Leave the cave\n>")

        if exit == "1":
            text_cave_lookaround()
        elif exit == "2":
            event_small_room()
        elif exit == "3":
            event_leave()
        else:
            error()
            event_cave()
    else:
        var_loop_count =0
        chase_monster = False
        small_unlocked = False
        print("You are in a cave\nYou dont know where you are\n")
        exit = input("\nCurrent Options:\n1. Stay in the cave\n2. Leave the cave\n>")

        if exit == "1":
            event_stay()
        elif exit == "2":
            event_leave()
        elif exit == "wake up":      #secret option
                death_ending("Waking up", "You shouldn't slam your head into rocks\nThat won't help you escape")
        else:
            error()
            event_cave()

def event_stay():
    dashes()
    print("You decided you will stay in the cave")
    stay = input("\nCurrent Options:\n1. Look around the cave\n2. Leave the cave\n>")
    if stay == "1":
        event_cave_lookaround()
    elif stay == "2":
        event_leave()
    else:
        error()
        event_stay()






#path 1 functions
def event_leave():
    dashes()
    print("You left the cave\nYou now see that you are in a clearing in a forest")
    clearing = input("\nCurrent Options:\n1. return to the cave\n2. continue into the trees\n3. investigate the trees\n>")
    if clearing ==  "1":
        event_cave()
    elif clearing == "2":
        event_strait_path()
    elif clearing == "3":
        text_investigate_trees()
    else:
        error()
        event_leave()

def text_investigate_trees():
    half_dash()
    print("There is somthing off about the trees\nAll of the trees are the exact same\nNot just the trees but the scenery behind them too")
    clearing = input("\nCurrent Options:\n1. return to the cave\n2. continue into the trees\n>")
    if clearing ==  "1":
        event_cave()
    elif clearing == "2":
        event_strait_path()
    else:
        error()
        text_investigate_trees()

def event_strait_path():
    dashes()
    print("Ahead of you the path seems to continue endlessly\nThe trees mirror eachother on both sides\nYou hear the sound of trees break behind you")
    path = input("\nCurrent Options:\n1. Continue onward\n2. turn around\n3. leave path\n>")
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
    print("Turning, around you see that the trees behind you have all fallen down\nYou have no way back")
    if input("1. turn around\n>") == "1":
        event_strait_path()
    else:
        error()
        event_strait_path()

def event_loop():
    global var_loop_count
    dashes()
    print("The path seems to strech endlessly")
    loop_path = input("\nCurrent Options:\n1. Continue forward\n2. Turn around\n3. Leave path\n>")
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
    moon_path = input("\nCurrent Options:\n1. take the left path\n2. take the right path\n>")
    if moon_path == "1":
        dashes()
        print("RESPAWN ACTIVATED")
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
        while True:
            half_dash()
            replay = input("choose an option to continue\n1. Try again from return\n2. Restart story\n>")
            if replay == "1":
                dashes()
                event_chase()
            elif replay == "2":
                print("\n"*10)
                event_cave()
            else:
                error()
   
    elif "run" in chase_action or "flee" in chase_action or "bolt" in chase_action:
        event_chase_run()
    
    elif "fight" in chase_action or "attack" in chase_action:
        half_dash()
        print("You attempt to fight the monster\nYou did well considering you were empty handed\nHowever it was all for naught\nBefore all fades to black you hear the beast release a wretched scream and thump onto the earth")
        while True:
            half_dash()
            replay = input("choose an option to continue\n1. Try again from return\n2. Restart story\n>")
            if replay == "1":
                dashes()
                event_chase()
            elif replay == "2":
                print("\n"*10)
                event_cave()   
            else:
                error()

    else:
        half_dash()
        print("In fear of the monster you couldn't think clearly and it killed you\n\n[Hint: Try entering a simple and relevant action]\n")
        while True:
            half_dash()
            replay = input("choose an option to continue\n1. Try again from return\n2. Restart story\n>")
            if replay == "1":
                dashes()
                event_chase()
            elif replay == "2":
                print("\n"*10)
                event_cave()
            else:
                error()
   
def event_chase_run():
    if var_loop_count > 15:
        death_ending("exaustion", "maybe dont walk so much before needing to run from a monster") 
    else:
        dashes()
        print("you run away from the monster\n after some running you approch an intersection")
        runaway_path = input("Current options\n1. Run to the left\n2. Run to the right\n>")
        if runaway_path == "1":
            event_chill()
        elif runaway_path == "2":
            half_dash()
            print("you ran to the right forgetting that that was the route you came from\nYou reach the strait path and continue to run\nThe moment you start to slow it seems the monster is immediatly behind you\nEvery thing fades to black")
            while True:
                half_dash()
                replay = input("choose an option to continue\n1. Try again from return\n2. Restart story\n>")
                if replay == "1":
                    dashes()
                    event_chase()
                elif replay == "2":
                    print("\n"*10)
                    event_cave()
                else:
                    error()

def event_chill():
    dashes()
    if chase_monster:
        print("the danger has passed\nBehind you the monster continues running down the other path\nIts shreiks gradually fading behind you")
        half_dash()
    print("It is getting cold now\nA mist forms with each breath")
    chill_action = input("\nCurrent Options:\n1. Continue onward\n2. attempt to find warmth\n>")
    if chill_action == "1":
        ending_forest_1()
    elif chill_action == "2":
        event_warmth()
    else:
        error()
        event_chill()

def event_warmth():
    dashes()
    print("You manage to find a blanket\nIt has gotten colder but maybe it would allow you to get some rest")
    warmth_action = input("\nCurrent Options:\n1. Take a rest\n2. Continue onward\n>")
    if warmth_action == "1":
        ending_forest_2()
    elif warmth_action == "2":
        if chase_monster:
            ending_forest_3()
        else:    
            ending_forest_2()
    else:
        error()
        event_warmth()    

def ending_forest_1():
    dashes()
    print("You find yourself in a small town\nYour town\nOn your doorstep your parents stand there expectantly\n")
    while True:
        var_32147836412 = input("Go Home?\n1. Yes\n2. No\n>")
        if var_32147836412 == "1":
            print(" - "*17)
            break
        else:
            half_dash()
            print("Take your time\nEnter 1 when ready\n")


    ending_dash()
    print("                Ending obtained:                   ")
    print("                     Home\n                        ")
    print("            You found your way home                ")
    print("      or.. at least you think you're home.\n        ")
    print("***************************************************")
    ending()
    print("\n"*5)

def ending_forest_2():
    dashes()
    print("You find yourself in a small town\nYour town\nNobody is here but you're to tired to care\nYou head strait to your bed\n")
    while True:
        var_32147836412 = input("Go to sleep?\n1. Yes\n2. No\n>")
        if var_32147836412 == "1":
            print(" - "*17)
            break
        else:
            half_dash()
            print("Take your time\nEnter 1 when ready\n")


    ending_dash()
    print("                Ending obtained:                   ")
    print("                    Alone\n                        ")
    print("         time for some well needed rest            ")
    print("    maybe tomorrow you'll look for your family.     ")
    print("***************************************************")
    print("\n"*5)
    ending()

def ending_forest_3():
    dashes()
    print("You find yourself in a small town\nYour town\nthe corpes of everyone you knew lay everywhere\nno doubt the monster's fault\nYou dont think you can handle this anymore\n")
    while True:
        var_32147836412 = input("wake up?\n1. Yes\n2. No\n>")
        if var_32147836412 == "1":
            print(" - "*17)
            break
        else:
            dashes()
            print("You head strait to your bed\n")
            while True:
                var_32147836412 = input("Go to sleep?\n1. Yes\n2. No\n>")
                if var_32147836412 == "1":
                    print(" - "*17)
                    break
                else:
                    half_dash()
                    print("Take your time\nEnter 1 when ready\n")


            ending_dash()
            print("                Ending obtained:                   ")
            print("                    Alone\n                        ")
            print("         time for some well needed rest            ")
            print("    maybe tomorrow you'll look for your family.     ")
            print("***************************************************")
            print("\n"*5)
            ending()

    ending_dash()
    print("this is the end then                               ")
    print("                  you slam you head into a rock    ")
    print("maybe that will stop this                          ")
    print("   maybe this nightmare will end.                 \n")
    print("                 Dream No More                     ")
    print("                Ending obtained\n                  ")
    print("***************************************************")
    print("\n"*5)
    ending()

def ending():
    pause = input("\nEnter to continue>")
    dashes()
    print("YOU WIN (kinda)\nthanks for playing\n")
    restart = input("Play Again?\n1. yes\n2. no\n>")
    if restart == "1":
        print("\n"*20)
        event_cave()
    else:
        print("i'll take that as a no")
        sys.exit("see you later")

def death_ending(cause,text):
    ending_dash()
    print(f"You died")
    print(f"cause of death:")
    print(cause)
    print(text)
    print("***************************************************")
    print("\n"*5)
    dashes()
    while True:
        restart = input("Type 1 to restart\n>")
        if restart == "1":
            print("\n"*20)
            event_cave()
        if restart == "2":
            sys.exit("see you later")
        else:
            half_dash()
            print("Rather than not typing 1\nyou can type 2 to end game")
    death_ending(death_cause, death_text)
'''
----the great divide------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----the great divide------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----the great divide------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

#more variables 
dining_room_name = "front left room"
nest_room_name = "right room"
lab_room_name = "Hallway"
oneway_room_name = "mysterious room"

max_health = 100
current_health = 100
inventory = set()

key_obtained = False
current_tool = None

frog_count = 0
frog_max = 5

nest_tool_located = False

current_location = None
dinner_tool = "axe"
nest_tool = "pickaxe"

def status():
    half_dash()
    print(f"Health: {current_health}/{max_health}")
    print(f"Inventory:\n{ "-Inventory empty" if inventory == [] else " -".join(inventory)}")
    pause = input("\nEnter to return>")
    print(" - "*17)

def save():
    pass
def load():
    pass

def event_cave_lookaround():
    global small_unlocked
    small_unlocked = True
    dashes()
    print("As you look around you bump into the wall and it crumbles\nbehind the wall is a smaller room")
    look_around = input("\nCurrent Options:\n1. Investigate the smaller room\n2. Continue looking around in the larger room\n3. leave the cave\n>")
    if look_around == "1":
        event_small_room()
    if look_around == "2":
        text_cave_lookaround()
    if look_around == "3":
        event_leave()
    else:
        error()
        event_cave_lookaround()

def text_cave_lookaround():
    half_dash()
    print("The walls are not very stable\nIt seems they could fall at any moment")
    choice = input("\nCurrent Options:\n1. Investigate the small room\n2. Leave the cave\n>")
    if choice == "1":
        dashes()
        event_small_room()
    elif choice == "2":
        event_leave()
    else:
        error()
        text_cave_lookaround()

def event_small_room():
    global inventory
    print("There  are few features in the small room\nA large carpet in the center of the circular room\nFour empty large bookcases along the walls\nA desk with a clock on the wall above it")
    investigate_choice = input("Current options\n1. Investigate Carpet\n2. Investigate bookcases\n3. Investigate desk\n4. Investigate clock\n5. Return to the main room\n>")
    
    if investigate_choice == "1":
        half_dash()
        print("You search the carpet")
        if not key_obtained:
            print("Under the edge you find a key and take it")
            key_obtained = True
            inventory.add("key")
        else:
            print("there is nothing new")
        half_dash()
        event_small_room()
    
    elif investigate_choice == "2":
        half_dash()
        print("The forth bookshelf to the right of the desk was stuck and could not move\nNo mater what you do you could not move it\nAll bookshelves are empty\nTHe other bookshelves have nothing behind them.")
        half_dash()
        event_small_room()

    elif investigate_choice == "3":
        half_dash()
        print("You take a look at the desk\nThere is nothing on top or within its two drawers")
        half_dash()
        event_small_room()
    
    elif investigate_choice == "4":
        event_set_clock()

    elif investigate_choice == "5":
        event_cave()
    
    else:
        error()
        event_small_room()

def event_set_clock():
    dashes()
    print("You take a look at the clock\nIts hands are loose\nYou could probably fix it")
    time = input("Fix clock?\n1. Yes\n2. No\n>")
    if time == "1":
        save()
        text_cave_route_start()
    elif time == "2":
        event_small_room()
    else:
        event_set_clock()

def text_cave_route_start():
    global dining_room_name, nest_room_name, lab_room_name, oneway_room_name
    dashes()
    print("Gravel starts to fall as the room starts to shake\nThere is the sound of boulders falling in the main room\nA hole opens in the ceiling\nThe moon shines directly above\nyou leave the clock to go check out the main room\nMaybe you can set the time later")
    print("Boulders cover the entrance to the cave\nYou cannot leave without breaking them")
    half_dash()
    print("Two new paths have shown\nthemselves one to the left of the room with the clock\nOne to your right\nThe clock room is to your left")
    pause = input("\nEnter to continue>")
    dining_room_name = "front left room"
    nest_room_name = "right room"
    lab_room_name = "mysterious room"
    oneway_room_name = "mysterious room"
    room_main()

def event_entrance():
    dashes()
    print("The entrance is blocked by bolders\nMaybe if you had a tool you could get out")
    if True:
        pause = input("Enter to return to the main room\n")
        room_main()



def room_main():
    global current_location
    current_location = "main room"
    dashes()
    print("You are now in the main room")
    main_room_path = input(f"\nCurrent Options:\n1. Investigate the entrance\n2. go to the clock room\n3. go to the {dining_room_name}\n4. go to the {nest_room_name}\ncs. Check status\n>")
    if main_room_path == "1":
        event_entrance()
    if main_room_path == "2":
        dashes()
        room_clock()
    if main_room_path == "3":
        dashes()
        room_dinner()
    if main_room_path == "4":
        dashes()
        room_nest()
    if main_room_path == "cs":
        status()
        room_main()
    else:
        error()
        room_main()


def room_clock():
    global current_location, inventory 
    current_location = "clock room"
    if True:
        print("The clock, carpet, desk, and bookshelves remain")
        clock_choice = input("\nCurrent Options:\n1. Investigate \n2. Set the time\n3. Return to the main room\ncs. Check status\n>")

        if clock_choice == "1":
            while True:
                half_dash()
                investigate_choice = input("investigate options:\n1. The carpet\n2. The bookshelves\n3. the desk\n4. Cancel")
                if investigate_choice == "1":
                    print("You search the carpet")
                    if not key_obtained:
                        print("Under the edge you find a key and take it")
                        key_obtained = True
                        inventory.add("key")
                    else:
                        print("there is nothing new")
                    pause = input("\nEnter to continue>")
                    break

                elif investigate_choice == "2":
                    if True:
                        print("The forth bookshelf to the right of the desk was stuck and could not move\nNo mater what you do you could not move it\nAll bookshelves are empty\nTHe other bookshelves have nothing behind them.")
                        pause = input("\nEnter to continue>")
                    break

                elif investigate_choice == "3":
                    print("You take a look at the desk\nThere is nothing on top or within its two drawers")
                    pause = input("\nEnter to continue>")
                    break
                elif investigate_choice =="4":
                    break
                else:
                    error()


            half_dash()
            room_clock()

        elif clock_choice == "2":
            print("You Set the time to 12:00")
            save()
            room_clock()

        elif clock_choice == "3":
            room_main()
        
        elif clock_choice == "cs":
            status()
            room_clock()

        else:
            error()
            room_clock()

def room_dinner():
    global inventory, dining_room_name, current_tool, current_location 
    current_location = "dinner"
    if dinner_tool != None:
        print(f"You are in the {dining_room_name}")
        if dining_room_name == "front left room":
            print(f"the room appears to be some sort of dining room\nThere are four tables and a counter\nThere are 2 simple stools at each table\nthe {dinner_tool} sits pn the wall behind the counter")
            dining_room_name = "dining room"
        else:
            print(f"The {dining_room_name} remains the same")

        dinner_choice  = input("\nCurrent Options:\n1. Investigate\n2. Return to main room\ncs. check status\n>")
        
        if dinner_choice == "1":
            while True:
                investigate_option = input("Investigate options:\n1. The tables\n2. The counter\n3. The stools\n4. The axe\n5. Cancel\n>")
                half_dash()
                if investigate_option == "1":
                    print("the tables are part of the ground carved from the very cave floor you stand on\nStrangely you find skeletons on each of the tables")
                    pause = input("\nEnter to continue>")
                    break
                elif investigate_option == "2":
                    print("The counter is on the opsite end of the room as the entrance\nthe counter is part of the floor\nThe countertop is smooth and cool to the touch")
                    pause = input("\nEnter to continue>")
                    break
                elif investigate_option == "3":
                    print("the stools are sturdy and smooth to the touch\nEach stool is made of wood")
                    pause = input("\nEnter to continue>")
                    break
                elif investigate_option == "4":
                    event_tool_found()
                    break
                elif investigate_option == "5":
                    break
                else:
                    error()
            half_dash()
            room_dinner()
        elif dinner_choice == "2":
            room_main()
        elif dinner_choice == "cs":
            status()
            room_clock()
        else:
            error()
            room_clock()
    else:
        print(f"The {dining_room_name} remains the same")
        dinner_choice  = input("\nCurrent Options:\n1. Investigate\n2. Return to main room\ncs. check status\n>")
        if dinner_choice == "1":
            while True:
                investigate_option = input("Investigate options:\n1. The tables\n2. The counter\n3. The stools\n4. Cancel\n>")
                half_dash()
                if investigate_option == "1":
                    print("the tables are part of the ground carved from the very cave floor you stand on\nStrangely you find skeletons on each of the tables")
                    pause = input("\nEnter to continue>")
                    break
                elif investigate_option == "2":
                    print("The counter is on the opsite end of the room as the entrance\nthe countker is part of the floor\nThe countertop is smooth and cool to the touch")
                    pause = input("\nEnter to continue>")
                    break
                elif investigate_option == "3":
                    print("the stools are sturdy and smooth to the touch\nEach stool is made of wood")
                    pause = input("\nEnter to continue>")
                    break
                elif investigate_option == "4":
                    break
                else:
                    error()
            half_dash()
            room_dinner()

def room_nest():
    global inventory, nest_room_name, current_location, nest_tool_located
    current_location = "nest"
    if True:
        print(f"you are in the {nest_room_name}")
        if nest_room_name == "right room":
            print("The right room is a large room\nThe floor is dirt rather than stone\nIt looks vaguely like a bids nest there are branches around the entire perimeter\nThere is a hall to the right")
            nest_room_name = "nest"
        else:
            print(f"the {nest_room_name} remains the same as before\nthe hall remains on the right")
        
        nest_choice = input(f"\nCurrent options:\n1. Search the nest\n2. Return to the main room\n3. go to the {lab_room_name}\ncs. Check status\n>")
        half_dash()
        if nest_choice == "1":
            next_finding = random.randint(1,20)
            if next_finding >= 19:
                print("In the stick you find something magical\n\nYou find a spinning frog in a cool hat")
            if next_finding >= 12 or nest_tool_located:
                nest_tool_located = True
                event_tool_found()
            else:
                print("you did not find anything")
                room_nest()
       
        if nest_choice == "2":
            room_main()
        if nest_choice == "3":
            event_locked_door()
        if nest_choice == "cs":
            status()
            room_nest()
        else:
            error()
            room_nest()


def event_tool_found():
    half_dash()
    global current_location,nest_tool,dinner_tool
    if current_location == "nest":
        print(f"You find the {nest_tool} in the nest")
        if current_tool != None:
            print("You cannot store both tools")
            tool_choice = input(f"swap the {current_tool} for the {nest_tool}\n1. Yes\n2. No\n>")
            if tool_choice == "1":
                print(f"You take the {nest_tool}")
                temp_tool = current_tool
                current_tool = nest_tool
                nest_tool = temp_tool
                pause = input("\nEnter to continue>")
                return
            elif tool_choice == "2":
                return
        elif current_tool == None:
            tool_choice = input(f"Take the{nest_tool}\n1. Yes\n2. No\n>")
            if tool_choice == "1":
                print(f"You take the {nest_tool}")
                temp_tool = current_tool
                current_tool = nest_tool
                nest_tool = temp_tool
                pause = input("\nEnter to continue>")
                return
            elif tool_choice == "2":
                return

    if current_location == "dinner":
        print(f"You go to the {dinner_tool} on the wall")
        if current_tool != None:
            print("You cannot store both tools")
            tool_choice = input(f"swap the {current_tool} for the {dinner_tool}\n1. Yes\n2. No\n>")
            if tool_choice == "1":
                print(f"You take the {dinner_tool}")
                temp_tool = current_tool
                current_tool = dinner_tool
                dinner_tool = temp_tool
                pause = input("\nEnter to continue>")
                return
            elif tool_choice == "2":
                return
        elif current_tool == None:
            tool_choice = input(f"Take the{dinner_tool}\n1. Yes\n2. No\n>")
            if tool_choice == "1":
                print(f"You take the {dinner_tool}")
                temp_tool = current_tool
                current_tool = dinner_tool
                dinner_tool = temp_tool
                pause = input("\nEnter to continue>")
                return
            elif tool_choice == "2":
                return



def event_locked_door():
    pass
