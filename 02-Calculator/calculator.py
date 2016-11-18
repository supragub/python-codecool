def getInput():
    usrInput1 = input("Enter a number (or a letter to \033[1mexit\033[0m): ")
    try:
        a = int(usrInput1)
        usrOperator = input("Enter an operator: ")
        usrInput2 = input("Enter another number: ")
        calculate(usrInput1, usrInput2, usrOperator)
    except ValueError:
        exit()

def calculate(a, b, o):
    a = int(a)
    b = int(b)

    if o == "+":
        res = a + b
    elif o == "-":
        res = a - b
    elif o == "*":
        res = a * b
    elif o == "/":
        res = a / b
    elif o == "**":
        res = a ** b
    else:
        res = "Operator error"

    print("Result: " + str(res))
    print("")

i = 1
while i == 1:
    getInput()