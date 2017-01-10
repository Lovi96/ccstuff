import random


def fill_list_of_nums(how_many_nums):
    # Fills a list with given number of multiples of 10.
    list_of_nums = []
    for i in range(how_many_nums):
        list_of_nums.append((i + 1) * 10)
    print(list_of_nums)
    return list_of_nums


def sum_dividable_by_20(list_of_nums):
    # Print the sum of all 20 dividable numbers from a give list.
    sum_of_divisible_nums = 0
    for num in list_of_nums:
        if num % 20:
            sum_of_divisible_nums += num
    print("Summation of number divisible by 20 is: " + str(sum_of_divisible_nums))


def main():
    number_list = fill_list_of_nums(20)
    sum_dividable_by_20(number_list)

if __name__ == "__main__":
    main()
