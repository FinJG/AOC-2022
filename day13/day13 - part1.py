pairs = []

with open("input.txt") as file:
    f = [eval(i) if i else "" for i in file.read().strip().splitlines()]
    f1 = [i for i in f if i]

    for i, v in enumerate(f):
        if (i + 1) % 3 == 0:
            pairs.append(f[i-2:i])
    pairs.append(f[i-1:i+1])
    for x, pair in enumerate(map(lambda x: zip(x[0], x[1]), pairs)):
        for y, each in enumerate(pair):
            if type(each[0]) != type(each[1]):
                if type(each[0]) == int:
                    pairs[x][y][0]  = [each[0]]
                else:
                    pairs[x][y][1]  = [each[1]]
   

def compare(left, right):
    left = left if type(left) == list else [left]
    right = right if type(right) == list else [right]
    for left2, right2 in zip(left, right):
        if isinstance(left2, list) or isinstance(right2, list):
            rec = compare(left2, right2)
        else:
            rec = right2 - left2
        if rec != 0:
            return rec
    return len(right) - len(left)


print( sum([i+1 for i, v in enumerate(pairs) if compare(v[0],v[1]) > 0]) ) 