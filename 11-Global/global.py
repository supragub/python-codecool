x = False

def kapcs(y):
    #global valtozo
    if y == False:
        y = True
        print("False")
    else:
        y = False
        print("True")
    return y

while True:
    a = input()
    if a == "x":
        kapcs(x)
