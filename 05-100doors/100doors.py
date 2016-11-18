
doorList = [0 * x for x in range(101)]

doors = "The following doors are open: "

for b in range(1,101):
    for a in range(1,101):
        if a % b == 0:
            if doorList[a] == 0:
                doorList[a] = 1
            else:
                doorList[a] = 0

for c in range(100):
    if doorList[c] == 1:
        doors = doors + str(c) + ", "

doors = doors + ","
doors = doors.replace(", ,", "")
print (doors)