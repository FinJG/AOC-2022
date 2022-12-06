with open("input.txt") as file:
    f = file.readlines()[0]
    for i in range(len(f)): 
        hold = f[i:i+4]
        if len(hold) == len(set(hold)):
            print(i+4)
            break
