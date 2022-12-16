pairs = []

with open("input.txt") as file:
    f = [eval(i) if i else "" for i in file.read().strip().splitlines()]
    f1 = [i for i in f if type(i) == list] + [[2]] + [[6]]
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


def sort(f1):
    index1 = 0
    index2 = 1    
    for loop in f1:
        if compare(f1[index1], f1[index2]) > 0:
            hold = f1[index1]
            f1[index1] = f1[index2]
            f1[index2] = hold
        index1 += 1
        index2 += 1
        if index2 == len(f1):
            index1 = 0
            index2 = 1
    return f1

for loop in range(len(f1)):
    f1 = sort(f1)

print((f1[::-1].index([6])+1) * (f1[::-1].index([2])+1)) 
