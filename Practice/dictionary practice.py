things = {
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