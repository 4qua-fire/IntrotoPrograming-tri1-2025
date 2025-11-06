fruit = ["orange","peach","mango","kiki","watermelon", "apple", "apple"]
print(fruit[0], fruit[-1])
fruit.append(input("choose a fruit to add\n>").lower())
fruit.remove(input(("choose a fruit to remove\n>").lower()))
fruit.sort()
print(fruit)
print(fruit.count("apple"))
for item in fruit:
    print(item)






#arr = [
#    [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9],
#    ]
#    ,
#    [
#    [10, 11, 12],
#    [13, 14, 15],
#    [16, 17, 18],
#    ]
#]
#
#print(arr[0][1])
#
#fav_food = ["Egg Benny", "Carbonara", "Cheeseburger"]
#fav_candy = ["Watermeloon Sour Patch Kids","Reese's", "Pull n Peel"]
#cool_drugs =[]
#
#print(fav_food[-1])
#
#fav_food.append("Pizza")       #- Adds item at end of list
#fav_food.remove("Pizza")       #- Removes first item in a list
#fav_food.insert(1,"Pizza")     #- Adds item at position
#fav_food.extend(fav_candy)     #- Adds list to the end of list
#
#fav_food.pop(1)                #- Removes and returns specific index
##fav_food.clear()              #- Removes every item in the list
#
#fav_food.sort(reverse = True)           #- Sorts the list (alphabetical or value) in decending order
#fav_food.index("Carbonara")    #- Returns index of item
#print(len(fav_food))                  #- Returns the length of the list
#
#numbers =[1,2,3,4,5,6]
#max(numbers)
#min(numbers)