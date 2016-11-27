import csv

f = open("test.txt", mode="r")
data = f.readlines()
print(data)
listofwords = []
dictofwords = {}
line_proper = ""
linelist = []
print(linelist)
for line in data:
    line_proper = data.strip("\n")
linelist = line_proper.split(sep=" ")
for word in (data):
    listofwords.append(word)
for words in listofwords:
    if words in dictofwords:
        dictofwords[words] += 1
    else:
        dictofwords.update({words: 1})
print(listofwords)
print(dictofwords)
