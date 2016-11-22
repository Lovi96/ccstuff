elems_number = int(input("How many elements do you want?"))
number_list = []

for i in range(elems_number):
    number_list.append(int(input("Gib numbah")))
maxi = 0
mini = number_list[0]
for num in number_list:
    if mini > num:
        mini = num
    if maxi < num:
        maxi = num

delta = maxi - mini
print(delta)
