fw = open("workfile.txt", "w")
fw.write("workfile tartalma")
fw.close()

fr = open("workfile.txt", "r")
sztring = fr.read()
print(sztring)
fr.close()
