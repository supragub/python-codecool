import random

number = "0123456789"
word = "abcdefghijklmnopqrstuvwxyz"
special = "!@#$%^&*()?"
lenght = 8


def passwordgen(dif=0):

    if dif == 0:
        lenght = 8

    elif dif == 1:
        lenght = 12

    elif dif == 2:
        lenght = 16

    password = ""
    lastlist = 0
    for i in range(0, lenght):
        if lastlist == 0:
            password = password + random.choice(number)
            lastlist = lastlist + 1
        elif lastlist == 1:
            password = password + random.choice(word)
            lastlist = lastlist + 1
        elif lastlist == 2:
            password = password + random.choice(word).upper()
            lastlist = lastlist + 1
        elif lastlist == 3:
            password = password + random.choice(special)
            lastlist = 0

    return password


def main():
    return


if __name__ == '__main__':
    main()
