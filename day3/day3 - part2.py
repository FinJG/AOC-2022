score = 0

with open("input.txt") as file:
    f = file.read().strip().splitlines()
    for line in [f[i:i + 3] for i in range(0, len(f), 3)]:
        for letter in line[0]:
            if letter in line[1] and letter in line[2]:
                if letter.islower():
                    score += ord(letter) - 96
                else:
                    score += ord(letter) - 38
                break

print(score)
