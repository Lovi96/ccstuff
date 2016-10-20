import math
seqNum=int(input("How many numbers would you like to see?"))
print("Fibonacci sequence for {} numbers: ".format(seqNum))
sorszam=0
num1=0
num2=1
fib = num1 + num2
for i in range(seqNum):
    sorszam+=1
    fib=num1+num2
    num1=num2
    num2=fib
    print("{}. {}".format(sorszam,num1))