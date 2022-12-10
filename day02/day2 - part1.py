dic = {
    "A X":4,
    "A Y":8,
    "A Z":3,
    "B X":1,  # this dictionary contains every pissible
    "B Y":5,  # hand that can be played and the
    "B Z":9,  # corrosponding points that they give
    "C X":7,
    "C Y":2,
    "C Z":6,
}

score = 0
with open("input.txt") as i:
    for line in i.read().strip().splitlines(): # loops through each line in the file
        score += dic[line] # adds the score of each hand to a variable
print(score)
