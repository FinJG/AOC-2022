x = 1
num = 20
add = 0
lis = []
with open("input.txt") as file:
    f = file.read().strip().splitlines()
    for i, loop in enumerate(f):
        if loop.startswith("addx"):
            x += int(loop.split()[1])
            add += 1
        if i + add == num or i + add == num-1:
            lis.append(x*num)
            num+= 40
print(sum(lis))