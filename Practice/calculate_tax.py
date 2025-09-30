#create a function to calculate tax
def calculate_tax(item,price,rate):
    print(f"item: {item}")
    print(f"tax: {price*rate}")
    print(f"total cost: {price+price*rate}")

#choose items
item = "compter" #random item
price = 300 #random price
rate = 0.06875 #minnesota tax rate of 6.875%

#run the functions
calculate_tax(item,price,rate)