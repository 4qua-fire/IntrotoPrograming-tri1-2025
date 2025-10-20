import random

def  fortune_seed():
    print(f"\n\n\n{"-"*7}Fortune Teller{"-"*43}")
    lucky = input("What is your lucky integer\n>")
    unlucky = input("what is your unlucky integer\n>")
    future = input("As a  decimal, how many years do you want to see into the future\n>")
    present =  input("As a  decimal, how old are you\n>")
    multi = input("Choose a decimal to be your magical multiplier\n>")
    try:
        lucky = int(lucky)
        unlucky = int(unlucky)
        future = float(future)
        present = float(present)
        multi = float(multi)
        if future >= 150:
            print("you will die")
            fortune_seed()
        return ((future/lucky)/3.14)*(multi%50)*(unlucky+present)
    except:
        print("-"*20)
        print("Imput error\nPlease try again")
        print("-"*20)
        fortune_seed()


#fortunes
f1= "someone will die"
f2= "you will earn money"
f3= "you will see another person"
f4= "you will read somthing"
f5= "someone will see you"
f6= "somthing unexpected will happen"
f7= "somthing you have planned will happen"
f8= "the sun will rise"
f9= "your heart will beat at least once "
f10="you will survive an unspecified amount of time"





seed = fortune_seed()
random.seed(seed)
fortunes = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10]
print(random.choice(fortunes))




