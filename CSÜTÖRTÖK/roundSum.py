def get_num():
    nums = []
    nums.append(int(input("1st numbah ")))
    nums.append(int(input("2st numbah ")))
    nums.append(int(input("3st numbah ")))
    return nums


def do_math(nums):
    for num in nums:
        if int(num) >= 5:
            remainder = 10 - num
            number += remainder
