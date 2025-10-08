number =  5
if number > 0:                              #if is needed for else
    print(f"{number} is positive")
else:                                       #else not needed for if
    print(f"{number} is not positive")

a=0
b=11
c=52

if True:
    print("if statement 1 ran")

if a==0:
    print("kiwi")
else:
    print("plum")


def password_input():
    real_password ="silksongisabsolutlyamazingandissuperdupercool"
    submited_password =input("password:")

    if real_password == submited_password:
        print("Access Granted")
    else:
        print("Access Denied")
        password_input()

password_input()