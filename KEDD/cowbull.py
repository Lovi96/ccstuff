import random


random_number = random.randint(1000, 9999)
print(random_number)
random_number = str(random_number)
while True:
    cow = 0
    bull = 0
    user_number = (input("agyál számt"))
    for num in range(0, 4):
        if user_number[num] in random_number:
            cow += 1
        if random_number[num] == user_number[num]:
            cow -= 1
            bull += 1
    print(cow, "cow")
    print(bull, "bull")
    if bull >= 4:
        print("Nyertél!")
        break
