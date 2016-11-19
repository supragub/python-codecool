import collections
from collections import OrderedDict


def orderDefault(inv):
    keyLength = 0
    valueLength = 0
    for k, v in inv.items():
        if valueLength < len(str(v)):
            valueLength = len(str(v))
        if keyLength < len(str(k)):
            keyLength = len(str(k))
    keyLength = int(keyLength)
    dashes = keyLength * 2 + valueLength * 2 - 2
    print("\nInventory:")
    print("  count" + " " * 4 + "item name")
    print("-" * dashes)
    for k, v in inv.items():
        a_v_len = (int(len(str(v))))
        a_k_len = (int(len(str(k))))
        frontspaces = (valueLength - a_v_len)
        spaces = (keyLength - a_k_len)
        print(" " * 3, " " * frontspaces, v, " ", " " * spaces, k)
    print("-" * dashes)


def orderSorted(inv):
    keyLength = 0
    valueLength = 0
    inv_1 = OrderedDict(sorted(inv.items(), key=lambda t: t[1], reverse=True))
    for k1, v1 in inv_1.items():
        if valueLength < len(str(v1)):
            valueLength = len(str(v1))
        if keyLength < len(str(k1)):
            keyLength = len(str(k1))
    keyLength = int(keyLength)
    dashes = keyLength * 2 + valueLength * 2 - 2
    print("\nInventory:")
    print("  count" + " " * 4 + "item name")
    print("-" * dashes)
    for k1, v1 in inv_1.items():
        a_v_len = (int(len(str(v1))))
        a_k_len = (int(len(str(k1))))
        frontspaces = (valueLength - a_v_len)
        spaces = (keyLength - a_k_len)
        print(" " * 3, " " * frontspaces, v1, " ", " " * spaces, k1)
    print("-" * dashes)


def orderReversed(inv):
    keyLength = 0
    valueLength = 0
    inv_2 = OrderedDict(sorted(inv.items(), key=lambda t: t[1]))
    for k2, v2 in inv_2.items():
        if valueLength < len(str(v2)):
            valueLength = len(str(v2))
        if keyLength < len(str(k2)):
            keyLength = len(str(k2))
    keyLength = int(keyLength)
    dashes = keyLength * 2 + valueLength * 2 - 2
    print("\nInventory:")
    print("  count" + " " * 4 + "item name")
    print("-" * dashes)
    for k2, v2 in inv_2.items():
        a_v_len = (int(len(str(v2))))
        a_k_len = (int(len(str(k2))))
        frontspaces = (valueLength - a_v_len)
        spaces = (keyLength - a_k_len)
        print(" " * 3, " " * frontspaces, v2, " ", " " * spaces, k2)
    print("-" * dashes)
