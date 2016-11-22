def get_potato_price():
    try:
        price = int(input("How much for a kilo of potato?"))
        return price
    except ValueError:
        return 0


def get_how_much_potato():
    try:
        kilos = int(input("How many kilos of potato?"))
        return kilos
    except ValueError:
        return 0
