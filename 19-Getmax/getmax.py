def getmax(a, b, c):
    if a > b > c:
        print(a, "is the biggest number")
    elif b > c > a:
        print(b, "is the biggest number")
    else:
        print(c, "is the biggest number")

getmax(1, 2, 3)
