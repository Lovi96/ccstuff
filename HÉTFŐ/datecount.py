def get_time1():
    time1 = input("Gib time plezs").split(".")
    return time1


def get_time2():
    time2 = input("Gib time2 plezs").split(".")
    return time2


def get_delta(time1, time2):
    delta1 = int(time1[0]) * 3600 + int(time1[1]) * 60 + int(time1[2])
    delta2 = int(time2[0]) * 3600 + int(time2[1]) * 60 + int(time2[2])
    returnValue = 0
    if delta1 >= delta2:
        returnValue = delta1 - delta2
        return returnValue
    else:
        returnValue = delta2 - delta1
        return returnValue


def main():
    print(get_delta(get_time1(), get_time2()))

main()
