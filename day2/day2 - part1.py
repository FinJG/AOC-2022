dic = {
    "A X\n":4,
    "A Y\n":8,
    "A Z\n":3,
    "B X\n":1,
    "B Y\n":5,
    "B Z\n":9,
    "C X\n":7,
    "C Y\n":2,
    "C Z\n":6,
}


score = 0
with open("input.txt") as f:
    for line in f.readlines():
        score += dic[line]       
print(score)
