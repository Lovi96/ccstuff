import math
seqNum=int(input("How many numbers would you like to see?"))
print("Fibonacci sequence for {} numbers: ".format(seqNum))
spaces=40
sorszam=0
num1=0
num2=1
fib = num1 + num2
for i in range(seqNum):
    sorszam+=1
    fib=num1+num2
    num1=num2
    num2=fib
    sorszamstring=str(sorszam)
    sorszamstringNum=len(sorszamstring)
    notspaces = str(fib)
    notspacNum=len(notspaces)
    print("{}.".format(sorszam), end="")
    for i in range((spaces - notspacNum) - sorszamstringNum):
        print(" ", end="")
    print("{}".format(fib))