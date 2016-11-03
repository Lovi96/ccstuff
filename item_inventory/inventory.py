import order
from order import *
import save
from save import *
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'dragon meat']
def controls():
    print("\nC for inventory\nO to sort inventory\nA for adding loot\nS to save inventory to .csv\nM to merge existing inventory with a predefined .csv\nQ to exit\n")
def allItems(inventory):   
    allItems = 0
    for v in inv.values():
        if allItems == 0:
            allItems = v
        else:
            allItems = int(allItems)
            v = int(v)
            allItems = allItems + v    
    print("Total: ", allItems)
def displayInventory(action):
    for k, v  in inv.items():
        print(v," ", k)    
    allItems(inv)
    print()
def addToInventory(inventory,addedItems):
    for k in dragonLoot:
        if k in inv:
            inv[k] = int(inv[k]) + 1
        else:
            inv.update({k:1})       
def printTable(inventory):
    sorting = input(str("Descending or Ascending sort (D/A): "))
    sorting = sorting[0].upper()
    if sorting == "D":
        orderSorted(inv)
    elif sorting == "A":
        orderReversed(inv)
    else:
        orderDefault(inv)
while True:
    action = (input("What would you like to do?(press H for help) : "))
    action = action[0].upper()
    if action == "C":
        print("\nHere you go chief:\n ")
        displayInventory(action)
    elif action == "O":
        printTable(inv)
    elif action == "A":
        addToInventory(inv, dragonLoot)
        print("Dragon loot has been added.")
    elif action == "S":
        saveInventory(inv, 'savedInventory.csv')
        allItems(inv)
    elif action == "H":
        controls()
    elif action == "M":
        impinv = {}
        impinv = importInventory('mergeInventory.csv')
        inv = mergeImportedList(inv, impinv)
    elif action == "Q":
        quit()