def find_min(numbers):
    if len(numbers) == 0:
        return numbers
    min = numbers[0]
    res = []
    for number in numbers:
        if number < min:
            min = number
            res = []
            res.append(min)
        elif number == min:
            res.append(min)
    return res
list_1 = [3, 3, 3, 2, 2, 2]
print(find_min(list_1))
