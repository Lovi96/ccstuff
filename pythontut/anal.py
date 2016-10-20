import sys
if len(sys.argv)>2:
    nev = sys.argv[1]
    print("Hello {1}{0}!".format(nev,sys.argv[2]))
elif len(sys.argv)>1:
    nev = sys.argv[1]
    print("Hello {}!".format(nev))
else:
    print("Hello World!")
