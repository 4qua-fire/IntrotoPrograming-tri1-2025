input("Hello!\nwelcome to my survey\n[TYPE ANY KEY TO CONTINUE]\n") #welcome the user to my survey

fav_animal =input("1. What is your favorite animal?\n>") #obtain the user's favorite animal
reason =input("2. why are they your favorite?\n>") #find why the user likes that animal
purpose =input("3. what is their purpose\n>") #find the animals purpose in this life
owned =input("4. do you own one?\n>") #find out if the user owns their favorite animal
size =input("5. how big is it?\n>") #learn the size of the animal
new_feature =input("6. what would make them better?\n>")  #learn what would make the animal better
color =input("7. what color are they?\n>") #learn the color of the animial
home =input("8. where do they live?\n>") #find where the animal lives 
diet =input("9. what do they eat?\n>") #learn the animal's diet
lifespan =input("10. how long do they live?\n>") #learn how long the animal live
#summerize the information learned 
print(f"your favorite animal is {fav_animal} because {reason}. when asked if you own one you said {owned}.\nthey are {size} and {color} and you think that {new_feature} would make them better.\nthey eat {diet}, live in {home}, and live for {lifespan}.  their purpose is too {purpose}")