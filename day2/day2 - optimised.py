score = 0
for line in open("input.txt").read().strip().splitlines():
    play = line.split(" ")
    myindex = "XYZ".index(play[1])
    score += (((myindex - ("ABC".index(play[0]) - 1)) % 3)* 3) + myindex + 1
print(score)
