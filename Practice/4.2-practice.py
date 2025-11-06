'''
games = ["Hollow Knight", "Hollow Knight: Silksong", "Minecraft", "The Legend of Zelda: Breath of the Wild", "The Legend of Zelda: Tear of the kingdom", "Slay the Spire", "Balatro"]
#for game in games:
#    print(game)

#every odd number less than 1 trillion in decending order
#for i in range(999999999,0, -2):
#    print(i)


for i in range(0,len(games)):
    print(games[i])

import random
numbers = []
for i in range(0,100):
    numbers.append(random.randint(-100,100))

#1 only positives
for num in numbers:
    if num > 0:
        print(num)
'''
import random


for i in range(10,0,-1):
    print(i)

numbers = [random.randint(0,10) for i in range(0,10)]
total = 0
for num in numbers:
    total += num
print(total)
#Better solution print(sum(numbers))

numbers = [i for i in range(1,6)]
square = []
for num in numbers:
    square.append(num**2)
print(square)
