import random


def fill_random_list(from_num, to_num):
    list_to_fill = []
    for i in range(10):
        list_to_fill.append(random.randint(from_num, to_num))
    return list_to_fill


def guessing_game(list_of_nums, smaller_num_list):
    counter = 0
    for i in range(20):
        if counter < 11:
            while list_of_nums[counter] != guess:
                guess = int(input("Enter an integer from {} to {}: ".format(min(list_of_nums), max(list_of_nums))))
                if guess < list_of_nums[counter]:
                    print("guess is low")
                elif guess > list_of_nums[counter]:
                    print("guess is high")
                else:
                    break
            print("you guessed it!")
            counter += 1
        else:
            while smaller_num_list[counter - 10] != guess:
                guess = int(input("Enter an integer from {} to {}: ".format(
                    min(smaller_num_list), max(smaller_num_list))))
                if guess < smaller_num_list[counter - 10]:
                    print("guess is low")
                elif guess > smaller_num_list[counter - 10]:
                    print("guess is high")
                else:
                    break
            print("you guessed it!")
            counter += 1


def main():
    list_of_nums = fill_random_list(1, 99)
    smaller_num_list = fill_random_list(1, 49)
    guessing_game(list_of_nums, smaller_num_list)


if __name__ == "__main__":
    main()
