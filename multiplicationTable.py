def get_numbah():
    number = int(input("Gib numbah plezs"))
    return number


def multiply_it(number):
    for i in range(1, 11):
        multiplied_number = i * number
        print("{} * {} = {}".format(i, number, multiplied_number))


def main():
    multiply_it(get_numbah())

main()
