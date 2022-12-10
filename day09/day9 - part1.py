X = 0
Y = 0
tail = [0, 0]
moves = [(0, 0)]
with open("input.txt") as file:
    f = file.read().strip().splitlines()
    
    for line in f:
        spl = line.split()

        for loop in range(int(spl[1])):
            if spl[0] == "R":
                X += 1
            if spl[0] == "L":
                X -= 1
            if spl[0] == "U":
                Y += 1
            if spl[0] == "D":
                Y -= 1

            if tail[0] < X and tail[1] < Y:
                if tail[0] + 2 == X or tail[1] + 2 == Y:
                    tail[0] += 1
                    tail[1] += 1
                    moves.append((tail[0],tail[1]))

            if tail[0] > X and tail[1] < Y:
                if tail[0] - 2 == X or tail[1] + 2 == Y:
                    tail[0] -= 1
                    tail[1] += 1
                    moves.append((tail[0],tail[1]))
            
            if tail[0] < X and tail[1] > Y:
                if tail[0] + 2 == X or tail[1] - 2 == Y:
                    tail[0] += 1
                    tail[1] -= 1 
                    moves.append((tail[0],tail[1]))           

            if tail[0] > X and tail[1] > Y:
                if tail[0] - 2 == X or tail[1] - 2 == Y:
                    tail[0] -= 1
                    tail[1] -= 1
                    moves.append((tail[0],tail[1]))


            while tail[0] < X-1:
                tail[0] += 1
                moves.append((tail[0],tail[1]))
            while tail[0] > X+1:
                tail[0] -= 1
                moves.append((tail[0],tail[1]))

            while tail[1] < Y-1:
                tail[1] += 1
                moves.append((tail[0],tail[1]))
            while tail[1] > Y+1:
                tail[1] -= 1
                moves.append((tail[0],tail[1]))


print(len(set(moves)))