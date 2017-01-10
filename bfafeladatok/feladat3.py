def get_nums():
    # Gets numbers from user standard input.
    list_of_nums = []
    for i in range(11):
        list_of_nums.append(int(input("Please enter a number")))
    return list_of_nums


def print_math(list_of_nums):
    # Prints math to standard output.
    for i in range(10):

        if i < 5:
            print(str(list_of_nums[i + 1] / list_of_nums[i]) + "\n\n")
        else:
            print(str(list_of_nums[i + 1] * list_of_nums[i]) + "\n\n")


def main():
    number_list = get_nums()
    print_math(number_list)


if __name__ == "__main__":
    main()
