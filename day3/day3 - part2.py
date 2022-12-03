import string

lis = []
alpha = list(string.ascii_letters)

with open("input.txt") as file:
    file = [[char for char in line][:-1] for line in file]
    for line in file:
        for index in alpha:
            if not file.index(line) % 3:
                backpack = file[file.index(line)-3:file.index(line)]
                if len(backpack) > 0:
                    if index in backpack[0] and index in backpack[1] and index in backpack[2]:
                        lis.append(index)


print(len(lis))
print(sum([alpha.index(i)+1 for i in lis]))
