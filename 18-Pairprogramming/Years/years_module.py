import datetime


def years(age):
    today = datetime.date.today()
    hundredyears = int(today.year) + (100 - age)
    return hundredyears


def main():
    name = input("Name: ")
    age = int(input("Age: "))
    print("Hi,", name, "You will be 100 old in", years(age))

if __name__ == '__main__':
    main()
