import os
import order
from order import *
import save
from save import *
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = [
    'gold coin',
    'dagger',
    'gold coin',
    'gold coin',
    'ruby']


def allItems(inventory):
    allItems = 0
    for v in inv.values():
        if allItems == 0:
            allItems = v
        else:
            allItems = int(allItems)
            v = int(v)
            allItems = allItems + v
    print("Total number of items:", allItems)


def display_inventory(action):
    for k, v in inv.items():
        print(v, k)
    allItems(inv)
    print()


def add_to_inventory(inventory, addedItems):
    for k in dragon_loot:
        if k in inv:
            inv[k] = int(inv[k]) + 1
        else:
            inv.update({k: 1})


def print_table(inventory):
    sorting = input(str("\nDo you want (D)escending or (A)scending sort?\n"))
    sorting = sorting[0].upper()
    if sorting == "D":
        orderSorted(inv)
        return allItems(inventory)
    elif sorting == "A":
        orderReversed(inv)
        return allItems(inventory)
    else:
        orderDefault(inv)
        return allItems(inventory)


os.system('clear')

while True:
    action = (
        input("\nAhoy, Mighty Pirate! What do you want?\n\n(C)heck your inventory\n(O)rder your inventory items\n(A)dd Dragoon loot to your inventory\n(S)ave your inventory items to paper (.csv)\n(M)erge your inventory items with your hidden items (.csv)\n(E)xit from the game\n"))
    action = action[0].upper()
    if action == "C":
        os.system('clear')
        print("\nInventory: ")
        display_inventory(action)
    elif action == "O":
        os.system('clear')
        print_table(inv)
    elif action == "A":
        os.system('clear')
        add_to_inventory(inv, dragon_loot)
        print(
            "\nDragon loot has been added to your inventory:\n", ', '.join(dragon_loot))
    elif action == "S":
        os.system('clear')
        export_inventory(inv, 'export_inventory.csv')
        allItems(inv)
    elif action == "M":
        os.system('clear')
        impinv = {}
        impinv = import_inventory('import_inventory.csv')
        inv = mergeImportedList(inv, impinv)
    elif action == "E":
        os.system('clear')
        print("Fair Winds, Mighty Pirate!")
        quit()
