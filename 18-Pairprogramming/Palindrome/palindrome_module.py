def palindrome(value):
    value = value.replace(" ", "")
    if str(value.lower()) == str(value.lower())[::-1]:
        print("True")
        return True
    else:
        print("False")
        return False


def main():
    palindrome(input("Check for palindrome: "))
    return

if __name__ == '__main__':
    main()
