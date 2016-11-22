'''global valtozo = False
def kapcs():
    if valtozo == False:
        valtozo = True
    else:
        valtozo = False
while True:
    a = input()
    if a == "x":
        kapcs()'''
file = open("./workfile.txt","r")
the_list = []

for line in file:
    szam = int(line.strip())
    the_list.append(szam+10)
file.close()
file2 = open("./workfile.txt","w")
for line2 in the_list:
    file2.write(str(line2) + "\n")
file2.close()

    