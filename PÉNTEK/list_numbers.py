def sum_numbers(list_given):
    sum_of_nums = 0
    counter = 0
    while counter < len(list_given):
        sum_of_nums += list_given[counter]
        counter += 1
    return sum_of_nums


def main():
    list_of_nums = [1, 2, 3, 4, 5, 6]
    print(sum_numbers(list_of_nums))

main()
