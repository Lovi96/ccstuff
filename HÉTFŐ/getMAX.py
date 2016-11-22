import sys


def get_max(num1, num2, num3):
    max_num = 0
    num_list = [num1, num2, num3]
    for i in num_list:
        if max_num <= int(i):
            max_num = int(i)
    return max_num


def main(num1, num2, num3):
    print(get_max(num1, num2, num3))

main(sys.argv[1], sys.argv[2], sys.argv[3])
