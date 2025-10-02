print("Calculator by benjamin\noperations:\naddition   subtraction   multiplication   division\nfloor division   exponentiation   modulus")

#operation functions
def add(x,y):           #add x and y
    return x+y
def subtract(x,y):      #subtract y from x
    return x-y          
def multiply(x,y):      #multiply x and y
    return x*y
def divide(x,y):        #divide x by y
    return x/y
def floor_divide(x,y):  #divide x by y and round down
    return x//y
def exponent(x,y):      #take x to the power of y
    return x**y
def mod(x,y):           #take the remainder of dividing x by y 
    return x%y

#my calculator is better than yours btw
def calculator():
    operation = input("operation:")
    x = int(input("number 1:"))
    y = int(input("number 2:"))
    if operation=="addition":           #add
        print(add(x,y))
    if operation=="subtraction":        #subtract
        print(subtract(x,y))
    if operation=="multiplication":     #multiply
        print(multiply(x,y))
    if operation=="division":           #divide
        print(divide(x,y))
    if operation=="floor division":     #floor divide
        print(floor_divide(x,y))
    if operation=="exponentiation":     #exponentiate
        print(exponent(x,y))
    if operation=="modulus":            #mod
        print(mod(x,y))
calculator()
