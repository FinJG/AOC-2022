print(sum([(ord(line[2]) - 154 - ord(line[0])) % 3 * 3 + ord(line[2]) - 87 for line in open("input.txt")]))
