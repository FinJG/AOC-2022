count = 0

with open("input.txt") as f:
    f = [[i.split("-") for i in line.split(",")] for line in f.read().strip().splitlines()]
    
    for loop in range(len(f)):
        sett1 = set(range(int(f[loop][0][0]), int(f[loop][0][1])+1))
        sett2 = set(range(int(f[loop][1][0]), int(f[loop][1][1])+1))

        if sett1.issubset(sett2) or sett2.issubset(sett1):
            count += 1

print(count)
