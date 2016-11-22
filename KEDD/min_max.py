import random
randomList = []
for i in range(0, 20):
    randomList.append(random.randint(0,200))
min = 52
iD = 0
numb = 0
for i in randomList:
    print(i)
    if(i < min):
        min = i
        iD = numb
    numb += 1
print("\nMin: {} \n id: ".format(min,iD))