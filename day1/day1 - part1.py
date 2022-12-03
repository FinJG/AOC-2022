lis = []
totals = []

with open("input.txt") as i:
    for loop in i.readlines():
        if len(loop) > 1:
            lis.append(int(loop))
        else:
            totals.append(sum(lis))
            lis = []

print sorted(totals)
