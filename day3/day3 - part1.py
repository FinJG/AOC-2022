score = 0

with open("input.txt") as file:
    for line in file:
        half = len(line) // 2
        for letter in line[:half]:
            if letter in line[half:]:
                if letter.islower():
                    score += ord(letter) - 96
                else:
                    score += ord(letter) - 38
                break

print(score)
