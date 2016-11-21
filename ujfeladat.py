from num_helper import *


def price_times_kilos():
    total_cost = get_how_much_potato() * get_potato_price()
    return total_cost


def main():
    cost = str(price_times_kilos())
    print("Total cost of potatoes: {} ft".format(cost))

main()
