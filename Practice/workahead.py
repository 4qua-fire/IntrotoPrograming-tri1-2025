#arithmetic aperators
5+3  #additionn            =8 
5-3  #subtracton           =2
5/3  #division             ~1.67
7//3 #division round down  ~2.34=2
5*3  #multiplication       =15
5**3 #exponentiation       =5^3=125
5%3  #modulus              =2
#modulus n%b : the remainder after dividing n by b or the last digit of n represented in base b

#connectation: connecting strings 
#varibles nemed with connect_name
connect_first_name = "Benjamin"
connect_last_name = "Aigbogun"
connect_age = 15
print('"Hello '+connect_first_name+" "+connect_last_name+' how old art thou?"')
str() #changes data to string format int for interger float for float 
print('"I am '+str(connect_age)+'"')

#formatted srings
print(f"Name: {connect_first_name} {connect_last_name}, Age: {connect_age}")
#it seem you add f to the beginning surround the variables/other data tpes in {} 

#Improper animal survey assignment practice
animal = "dog"
animal_reason = "they are cute"
animal_amount = "over 340 breeds"
animal_owned = "yes"
animal_size = "medium"
animal_new_size = "either way"
animal_color = "any color"
animal_home = "wherever humans are"
animal_diet = "almost anything"
animal_time = "10-13 years"
print("1. what is your favorite animal? "+animal+"s")
print(f"2. why are {animal}s your favorite? {animal_reason}")
print(f"3. how many types of {animal}s are there?  {animal_amount}")
print(f"4. do you own one? {animal_owned}" )
print(f"5. what's the size of {animal}s? {animal_size}")
print(f"6. would {animal}s be better bigger or smaller? {animal_new_size}")
print(f"7. what color are {animal}s? {animal_color}")
print(f"8. where do they live? {animal_home}")
print(f"9. would you eat a {animal}? {animal_diet}")
print(f"10. how long do they live? {animal_time}")
print()
print(f"your favorite animals are {animal}s. you {"own"} an {animal} and like {animal}s because {animal_reason}. \nthere are {animal_amount} that live {animal_home}. {animal}s eat {animal_diet}, are {animal_color}, and are {animal_size} sized. \nwhen asked if they would be better bigger or smaller you said {animal_new_size}. finally they live {animal_time} ")