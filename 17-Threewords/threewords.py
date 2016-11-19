def splitWords(text):
    words = text.split(" ")
    v = 0

    for i in words:
        if i.isdigit():
            v = 0
        else:
            v = v + 1

        if v > 2:
            return True
    return False


print(splitWords("Hello World hello"))
print(splitWords("He is 123 man"))
print(splitWords("1 2 3 4"))
print(splitWords("bla bla bla bla"))
print(splitWords("Hi"))
