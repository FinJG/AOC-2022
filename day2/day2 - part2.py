dic = {
    "A X":3,
    "A Y":4,
    "A Z":8,
    "B X":1,  # this dictionary contains all of the possible
    "B Y":5,  # combinations of hands that could be thrown
    "B Z":9,  # and the corrosponding points that they give
    "C X":2,
    "C Y":6,  # the only change in part2 of this challenge
    "C Z":7,  # are the values used in the dictionary 
}

score = 0
with open("input.txt") as i:
    for line in i.read().strip().splitlines(): # loops through each line in the file
        score += dic[line] # adds the score of each hand to a variable
print(score)
