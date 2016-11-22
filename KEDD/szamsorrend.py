num_list_range = int(input("HOw many numbahs"))
num_list = []
num_list_reversed = []
num_list_reversed_multiplied = []
number = 0
for i in range(num_list_range):
    num_list.append(int(input("Gib numbahs   ")))
for i in num_list:
    i = i * i
    num_list_reversed.append(i)
for i in range(num_list_range):
    number = num_list_reversed[num_list_range - i - 1]
    num_list_reversed_multiplied.append(number)
print(num_list)
print(num_list_reversed)
print(num_list_reversed_multiplied)
