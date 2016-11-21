def get_width():
    width = int(input("Give width"))
    return width


def get_height():
    height = int(input("Give height"))
    return height


def get_chartype():
    chartype = input("Give character")
    return chartype


def drawing():
    height = get_height()
    width = get_width()
    chartype = get_chartype()
    for i in range(0, height):
        print(chartype * width)


def main():
    drawing()

main()
