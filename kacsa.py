cucc = "ezt ne <de ezt igen> de ezt se <de tibi>"
newstring = ""
flag = 0
for i in cucc:
    if i == "<":
        flag = 1
    elif i == ">":
        flag = 0
    elif flag == 1:
        newstring += i
print(newstring)
