"""things = {
    "colors":["blue", "green", "red"],
    "something": "something",
    "nothing": []



}


print(things["colors"])

#add entry
things["foods"] = ["pizza", "potatos", "banana"]

#modify entry
things["colors"].append("purple")

#remove entry
del things["nothing"]
things.pop("something")


#.keys 
#.values
#.items
#.clear
"""
#1
grades ={
    "Alice": "A",
    "Bob": "B",
    "Charlie": "C",
    "David": "D",
    "Eve": "F"
}

#2
student ={
    "name": "Alice",
    "age": 16,
    "grade": "A"
}

print(f"Student: {student['name']}\nGrade: {student['grade']}")

#3
student["grade"] = "A+"

print(f"Student: {student['name']}\nGrade: {student['grade']}")

#4
movies={
    "askjlh": 1307,
    "poifgkl": 2983,
    "sporwel": 2013
    }
#x= input("movie: ")
#movies[x] = input("release date: ")

print(movies)

#5
fruit = {
    "apple": 10,
    "bannana": 11,
    "peach": 12,
    "watermelon": 19,
    "pear": 7
}
print(fruit)
x = input("Fruit to remove:")
if x in fruit:
    del fruit[x] 
print (fruit)

#6
for item in fruit.keys():
    print(f"{item}\nCost: {fruit[item]}\n")

#7
word_list = ["a", "a"]
count={}
for item in word_list:
    count[item] = word_list.count(item)
print(count)

#8
library ={
    "The adventures of the great Garmond": {"author": "zaza", "publication year":"2025"},
    "SHAW": {"author": "hornet", "publication year": "2017"}:
    "": {"author": "the knight", "publication year": "0"}
}

#9
squares = {}
for i in range(1,10):
    squares[i] = i*i