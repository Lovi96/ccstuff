def is_prime(number):
    if number == 0:
        print("ZÉRÓ")
        return False
    for num in range(2, number - 1):
        if number % num == 0:
            return False
    return True


def get_number():
    try:
        number = int(input("Gib numbah plox!"))
    except ValueError:
        print("I said numbaaah!")
    return number


def main():
    if is_prime(get_number()):
        print("Its a prime!")
    else:
        print("Its not a prime!")

main()
