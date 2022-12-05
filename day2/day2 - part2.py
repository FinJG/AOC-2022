dic = {
    "A X\n":3,
    "A Y\n":4,
    "A Z\n":8,
    "B X\n":1,
    "B Y\n":5,
    "B Z\n":9,
    "C X\n":2,
    "C Y\n":6,
    "C Z\n":7,
}

score = 0
with open("input.txt") as f:
    for line in i.readlines():
        score += dic[line]
print(score)
