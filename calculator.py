while True:
    try:
        num1 = int(input("Enter a number or a letter to exit "))
        operator = input("Enter an operator ")
        num2 = int(input("Enter another number "))
        if operator == "+":
            print("{} + {} = {}".format(num1, num2, num1+num2))
        elif operator == "-":
            print("{} - {} = {}".format(num1, num2, num1-num2))
        elif operator == "*":
            print("{} * {} = {}".format(num1, num2, num1*num2))
        elif operator == "/":
            print("{} / {} = {}".format(num1, num2, num1/num2))
        else:
            print("Use +,-,* or / next time!")
    except ValueError:
        break