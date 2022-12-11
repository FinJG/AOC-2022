count = 0
x = 1
y = 1
y2 = 0

with open("input.txt") as file:
    f = file.read().strip().splitlines()
    for line in f:
        for num in line:
            Xtrees = [-1] + [int(i) for i in line] + [-1]
            Ytrees = [-1] + [int(i[y2]) for i in f] + [-1]
            if int(num) > max(Xtrees[:x]) or int(num) > max(Xtrees[x+1:]) or int(num) > max(Ytrees[:y]) or int(num) > max(Ytrees[y+1:]):
                count += 1
            x += 1
            y2 += 1
        y += 1
        y2 = 0
        x = 1
print(count)

            
