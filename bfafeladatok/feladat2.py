import random


def fill_list_with_random(from_num, to_num, number_of_nums):
    # fills a list with random numbers
    list_of_nums = []
    for i in range(number_of_nums):
        list_of_nums.append(random.randint(from_num, to_num))
    print(list_of_nums)
    return list_of_nums


def search_divisible(list_of_nums):
    # prints out how many numbers are divisible by 7,5 or 3 in a give list.
    counter = 0
    for i in range(len(list_of_nums)):
        if list_of_nums[i] % 7 == 0 or list_of_nums[i] % 5 == 0 or list_of_nums[i] % 3 == 0:
            print(str(list_of_nums[i]) + " is divisible by 7 or 5 or 3!")
            counter += 1
    print("We found " + str(counter) + " numbers divisible by 7 or 5 or 3!")


def main():
    random_list = fill_list_with_random(1, 99, 10)
    search_divisible(random_list)

if __name__ == "__main__":
    main()
