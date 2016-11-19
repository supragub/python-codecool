
file = open("./file.txt", "r")

the_list = []

for line in file:
    szam = int(line.strip())
    the_list.append(szam + 10)

print(the_list)

file.close()
file2 = open("./file.txt", "w")

for line2 in the_list:
    file2.write(str (line2) + "\n")
file2.close()
