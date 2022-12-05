import string

alpha = list(string.ascii_letters)
lis = []

with open("input.txt") as file:
    for line in [[char for char in line][:-1] for line in file]:
        half = int(len(line)/2)
        for index in line[:half]:
            if index in line[half:]:
                lis.append(index)
                break

print(sum([alpha.index(i)+1 for i in lis]))
