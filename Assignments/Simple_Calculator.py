mode = "simple calculator" #make sure mode is set to the function that will be run
print("current mode: " + mode)
if mode == "simple calculator":
    print("Calculator by benjamin\n\noperations:\naddition   subtraction   multiplication   division\nfloor division   exponentiation   modulus")
x = float(input("number 1:"))
y = float(input("number 2:"))

#single operation functions
def add():           #add x and y
    return x+y
def subtract():      #subtract y from x
    return x-y          
def multiply():      #multiply x and y
    return x*y
def divide():        #divide x by y
    return x/y
def floor_divide():  #divide x by y and round down
    return x//y
def exponent():      #take x to the power of y
    return x**y
def mod():           #take the remainder of dividing x by y 
    return x%y

# calculate function allows the User to choose their opperation with an imput
def simple_calculator():
    operation = input("operation:")
    if operation == "addition":           #add
        print(add())
    if operation == "subtraction":        #subtract
        print(subtract())
    if operation == "multiplication":     #multiply
        print(multiply())
    if operation == "division":           #divide
        print(divide())
    if operation == "floor division":     #floor divide
        print(floor_divide())
    if operation == "exponentiation":     #exponentiate
        print(exponent())
    if operation == "modulus":            #mod
        print(mod())

#run a function here
simple_calculator() #make sure mode is set to the function that will be run
