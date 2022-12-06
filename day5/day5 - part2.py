import re

with open("input.txt") as f:
    moves = []
    for loop in f.read().strip().splitlines():
        moves.append(re.split("move ([0-9]+) from ([0-9]+) to ([0-9]+)", loop))
    f.seek(0)

    stack_data = f.readlines()[:8]
    stack_data = [i.replace("    ","_") for i in stack_data]
    stacks = [[], [], [], [], [], [], [], [], []]

    for index in stack_data[::-1]:
        count = 0
        for i in index:
            if (64 < ord(i) < 91):
                stacks[count].append(i)
                count += 1
            elif i == "_":
                count += 1

def move_boxes(amount, frm, to):
    for loop in stacks[frm][-amount:]:
        stacks[to].append(loop)
    stacks[frm][-amount:] = []

for loop in [[x for x in i if x] for i in moves if i][10:]:
    move_boxes(int(loop[0]), int(loop[1])-1, int(loop[2])-1)

print("".join([loop[-1] for loop in stacks]))
