def part1():
    with open("input2.txt") as f:
        lis, bis= [], []
        [lis.append(int(i)) if len(i) > 1 else [bis.append(sum(lis)), lis.clear()] for i in f]
        return sorted(bis)[-1]


def part2():
    with open("input2.txt") as f:
        lis, bis= [], []
        [lis.append(int(i)) if len(i) > 1 else [bis.append(sum(lis)), lis.clear()] for i in f]
        return sum(sorted(bis)[-3:])

print("part 1:", part1(), "\npart 2:", part2())