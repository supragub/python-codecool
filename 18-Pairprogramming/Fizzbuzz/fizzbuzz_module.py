def fizzbuzz(number):
    text = number
    if int(number) % 15 == 0:
        text = "FizzBuzz"
    elif int(number) % 3 == 0:
        text = "Fizz"
    elif int(number) % 5 == 0:
        text = "Buzz"
    return text
def main():
    for i in range(1, 101):
        print(fizzbuzz(i))
        fizzbuzz(i)
    return
if __name__ == '__main__':
    main()