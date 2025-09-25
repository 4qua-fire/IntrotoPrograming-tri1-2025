#2.3 -variables and imput
print("operations")
print(2+2) #add
print(2-2) #subtract
print(2*2) #multiply
print(2/2) #divide

print()
print("data types")

#string        -"in quotations"
#interger      -a whole number
#float         -a decimal number
#character     -a singal glyph
#boolean       -True or false

print("don't") #string
print(2)       #interger
print(3.14)    #float
print('c')     #character
print(True)    #boolean

print()
print("variables")

x=10
y=50
potato=7

print(x*y*potato)

#Naming conventions
lowercase = False
UPPERCASE = False
UpperCamelCase = False       #All lowercase, no spaces, capital for new words
lowerCamelCase = False       #All lowercase, no spaces, capital for new words
snake_case = True            #All lowercase, underscore for spaces
SCREAMING_SNAKE_CASE =False

#Other general rules to naming things
#1. Concise (short and discriptive)

#imput
#input("what is your name? ")
#print("complete")

name = (input("What is your name?\n>"))
print("your name is " + name)
print("cat"*10)

#get number as string
num = input("number to be squared?\n >")

#convert (parse) the string into an int (cast)
num = float(num)

#do math and print
print(num*num)