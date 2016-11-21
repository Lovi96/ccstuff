def addnumbers():
    num = 1
    for i in range(1, 101):
        num += i
    print(num)


def multiplynumbers():
    num = 1
    for i in range(1, 51):
        num *= i
    print(num)


def main():
    print(addnumbers())
    print(multiplynumbers())


main()
