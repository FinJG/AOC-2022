score = 0
for line in open("input.txt").read().strip().splitlines():
    myindex = ord(line[2]) - 88
    score += (((myindex - (ord(line[0]) - 66)) % 3)* 3) + myindex + 1
print(score)
