todo_list = []
file = "./todo.txt"


def add():
    text = input("Type: ")
    todo_list.append(text)
    saveFile()
    list()


def list():
    print("\nYour todo list:")
    for i in todo_list:
        print(" - " + i)


def mark():
    print("")


# mark

def archive():
    print("")


# archive

def saveFile():
    fileContent = open(file, "w")
    for i in todo_list:
        fileContent.write(str(i) + "\n")
    fileContent.close()


def readFile():
    fileContent = open(file, "r")
    for line in fileContent:
        todo_list.append(line.strip())
    fileContent.close()


readFile()
while True:
    command = input("Chosse a command[add, list, mark, archive]")

    if command == "add":
        add()
    if command == "list":
        list()
    elif command == "exit":
        break