def calculate_tax(item,price,rate):
   return(price*rate)

calculate_tax("dog",10.0,0.0685)


#funtion to add five numbers
def add_five_numbers (a,b,c,d,e):
    print(a+b+c+d+e)

add_five_numbers(1,2,3,4,5)
add_five_numbers(6,7,8,9,10)
add_five_numbers(11,12,13,14,15)

#funtion to print concatination of persons first and last name from an imput

def full_name(first,last):
    print(first+" "+last)

first_name = input("first name:")
last_name = input("last name:")
full_name(first_name,last_name)

#function that calulates the area based on lenthe and width
def area_calculator(length, width):
    print(length*width) #the instructions dont say print tho
area_calculator(1,2)
area_calculator(3,4)
area_calculator(5,6)

#function that concats 2 parmeter
def word_smash(a,b):
    print(str(a)+str(b))
word_smash("cat",3)
word_smash("house","dog")
word_smash("mean",17.02)

#function that prints a string a number of time 
def echo(string,number):
    print(str(string)*int(number))
echo("cat",10)

#happy birthday function says happy birthday to a name
def happy_birthday(name):
    print(f"happy birthday to you,\nhappy birthday to you,\nhappy birthday dear {name},\nhappy birthday to you.")
happy_birthday("Nolan Wayne Frater")
