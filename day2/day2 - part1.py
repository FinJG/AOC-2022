dic = {
    "A X\n":4,
    "A Y\n":8,
    "A Z\n":3,
    "B X\n":1,  # this dictionary contains every pissible
    "B Y\n":5,  # hand that can be played and the
    "B Z\n":9,  # corrosponding points that they give
    "C X\n":7,
    "C Y\n":2,
    "C Z\n":6,
}


score = 0
with open("input.txt") as f:
    for line in f.readlines(): # loops through each line in the file
        score += dic[line] # adds the score of each hand to a variable
print(score)
