import csv


def importInventory(importFile):
    impinv = {}
    row = 0
    file = open(importFile, "r")
    reader = csv.reader(file, quoting=csv.QUOTE_MINIMAL, doublequote=False)
    next(reader, None)
    impinv = dict((row[0], row[1])for row in reader)
    file.close()
    return impinv


def mergeImportedList(mainInventory, importedInventory):
    mergedinv = dict(mainInventory)
    importedinv = dict(importedInventory)
    for k in importedinv.keys():
        if k in mergedinv:
            mergedinv[k] = int(mergedinv[k]) + int(importedinv[k])
        else:
            mergedinv.update({k: importedinv[k]})
    print('Merging complete')
    return mergedinv


def saveInventory(inventory, filename):
    file = open(filename, "w")
    writer = csv.writer(open(filename, 'w'))
    writer.writerows(inventory.items())
    file.close()
    print("Inventory saved to .csv")
