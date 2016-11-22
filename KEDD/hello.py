import sys
def getName():
    #gets the second argument given and puts it after hello then exits the program
    nev = sys.argv[1]
    print("Hello {}!".format(nev))
    exit
def getArgs():
    '''gets the length of the list of arguments, if more than 1 returns true
    the name of the program is argument #1 thats why its needed to check for more than 1'''
    if len(sys.argv) > 1:
        return any
def helloWorld():
    #prints hello world on screen, then exits the program
    print("Hello World!")
    exit
#The program itself
if getArgs():
    getName()
else:
    helloWorld()