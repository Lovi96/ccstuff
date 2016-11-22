'''class Dog:
    def __init__(self, name="", height=0,weight=0):
        self.name = name
        self.height = height
        self.weight = weight
    def run(self):
        print("{} the dog runs".format(self.name))
    def eat(self):
        print("{} the dog eats".format(self.name))
    def bark(self):
        print("{} the dog barks".format(self.name))
def main():
    spot = Dog("SPot",66,26)
    spot.bark()
    spot.eat()
    spot.run()
main()'''


class Square:

    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    @property
    def height(self):
        print("Retrieving the height")
        return self.__height

    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("Please only enter numbers.")

    @property
    def width(self):
        print("Retrieving the width")
        return self.__width

    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Please only enter numbers.")

    def getArea(self):
        return int(self.__width) * int(self.__height)


def main():

    aSquare = Square()
    height = input("Enter a height: ")
    width = input("Enter a width: ")
    aSquare.width = width
    aSquare.height = height
    print("Height: ", aSquare.height)
    print("Width: ", aSquare.width)
    print("The area is : ", aSquare.getArea())

main()
