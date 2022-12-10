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

print(sum([dic[i] for i in open("input.txt")]))
