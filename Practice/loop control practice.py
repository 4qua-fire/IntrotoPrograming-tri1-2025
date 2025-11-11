'''
for i in range(1,21):
    if i == 15:
        break
    print(i)

for i in range(1,31):
    if not i%2:
        continue
    print(i)

for i in "Hello World":
    pass #Encode Hello World with the ceaser cypher and then multiply by 30,000 and turn each number into binary

for i in range(10,0,-1):
    if i == 5:
        continue
    print(i)
'''
import random
'''
for i in range(51):
    list = [random.randint(-10,10) for i in range(11)]
    total = 0
    for x in list:
        if x < 0:
            break
        total += x
    print(total)
'''
superlist = []
for i in range(11):
    new_list = []
    for i in range(51):
        number =[]
        for i in range(100001):
            list = [random.randint(-10,10) for i in range(10)]
            total = 0
            for x in list:
                if x < 0:
                    break
                total += x
            number.append(total)
        new_list.append(max(number))
    superlist.append(max(new_list))
print(max(superlist))