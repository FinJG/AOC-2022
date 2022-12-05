lis = []

with open("input.txt") as file:
    for line in file:
        half = len(line) // 2
        for index in line[:half]:
            if index in line[half:]:
                lis.append(index)
                break

print(sum([ord(i) - 96 if i.islower() else ord(i) - 38 for i in lis]))
