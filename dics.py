'''derekDict = {"fName":"Derek","lName":"Banas","address":"123 Main st."}
print("My name:", derekDict["fName"])
derekDict["address"]="215 main st."
derekDict["city"] = "pittsburg"
print("is there a city:","city" in derekDict)
print(derekDict.values())
print(derekDict.keys())
for k, v in derekDict.items():
    print(k,v)
print(derekDict.get("mName","Not here"))
print(derekDict.get("lName","Not here"))
del derekDict["fName"]
for i in derekDict:
    print(i)
derekDict.clear()
emloyees = []
fName, lName = input ("Enter employee names").split()
employees.append({"fName":fName,"lName":lName})
print(emloyees)'''
customers = []
while True:
    createEntry = input("Enter customer(Y/N): ")
    createEntry = createEntry[0].lower()
    if createEntry == "n":
        break
    else:
        fName, lName = input("Enter customer name: ").split()
        customers.append({"fName":fName,"lName":lName})
for cust in customers:
    print(cust["fName"],cust["lName"])
