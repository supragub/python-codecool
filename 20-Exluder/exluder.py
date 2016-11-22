def remove_duplicates():
    t = [1, 2, 3, 1, 2, 5, 6, 7, 8]
    t2 = []
    for i in t:
        if i not in t2:
            t2.append(i)
    print(t2)

remove_duplicates()
