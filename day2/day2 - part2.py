dic = {
    "A X\n":3,
    "A Y\n":4,
    "A Z\n":8,
    "B X\n":1,  # this dictionary contains all of the possible
    "B Y\n":5,  # combinations of hands that could be thrown
    "B Z\n":9,  # and the corrosponding points that they give
    "C X\n":2,
    "C Y\n":6,  # the only change in part2 of this challenge
    "C Z\n":7,  # is the values in the dictionary 
}

score = 0
with open("input.txt") as f:
    for line in i.readlines(): # loops through each line in the file
        score += dic[line] # adds each hands corrosponding value to a variable
print(score)
