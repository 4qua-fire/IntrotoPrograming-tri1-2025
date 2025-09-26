input("Hello!\nwelcome to my survey\n[TYPE ANY KEY TO CONTINUE]\n")

fav_animal =input("1. What is your favorite animal?\n>")
reason =input("2. why are they your favorite?\n>")
purpose =input("3. what is their purpose\n>")
owned =input("4. do you own one?\n>")
size =input("5. how big is it?\n>")
new_feature =input("6. what would make them better?\n>")
color =input("7. what color are they?\n>")
home =input("8. where do they live?\n>")
diet =input("9. what do they eat?\n>")
lifespan =input("10. how long do they live?\n>")

print(f"your favorite animal is {fav_animal} because {reason}. when asked if you own one you said {owned}.\nthey are {size} and {color} and you think that {new_feature} would make them better.\nthey eat {diet}, live in {home}, and live for {lifespan}.  their purpose is too {purpose}")