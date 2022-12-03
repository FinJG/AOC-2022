import string

alpha = list(string.ascii_letters)
lis = []

with open("input.txt") as file:
    file = [[char for char in line][:-1] for line in file]
    for line in file:
        for index in alpha:
            half = int(len(line)/2)
            if index in line[:half] and index in line[half:]:
                lis.append(index)

print(sum([alpha.index(i)+1 for i in lis]))