def feladat():
    the_list = []
    for i in range(0, 11):
        input_number = int(input("adjadmeg"))
        the_list.append(input_number)
    for i in range(0, len(the_list)):
        if i < 5:
            print(the_list[i + 1], "/", the_list[i], "=", (the_list[i + 1] / the_list[i]))
            print(" " * i)
        if i > 4 and i < 10:
            print(the_list[i + 1], "*", the_list[i], "=", (the_list[i + 1] * the_list[i]))
            print(" " * i)


def main():
    feladat()

main()
