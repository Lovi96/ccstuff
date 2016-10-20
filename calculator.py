import math
print("\nWelcome to the calculator script!\n")
while True:
    try:
        def inputNum2():
            global num2
            num2 = int(input("Enter another number: "))
        num1 = int(input("Enter a number or a letter to exit: "))
        operator = input("Enter an operator: ")
        if operator == "+":
            inputNum2()
            print("{} + {} = {}".format(num1, num2, num1+num2))
        elif operator == "-":
            inputNum2()
            print("{} - {} = {}".format(num1, num2, num1-num2))
        elif operator == "*":
            inputNum2()
            print("{} * {} = {}".format(num1, num2, num1*num2))
        elif operator == "/":
            inputNum2()
            print("{} / {} = {}".format(num1, num2, num1/num2))
        elif operator == "sqrt":
            print("{} √ = {}".format(num1, math.sqrt(num1)))
        else:
            print("Use +,-,*,/ or sqrt next time!\n")
    except ValueError:
        print("\nThanks for using this calculator!\n")
        break