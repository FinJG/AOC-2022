lis = []
totals = []

with open("input.txt") as file:
    
    for loop in file.readlines():      # loops through the file and adds
        if len(loop) > 1:           # every line that isnt empty to a list
            lis.append(int(loop))
            
        else:                       # if a empty line is found the sum of
            totals.append(sum(lis)) # the list is added to the "totals" list
            lis = []                # and then original list is cleared

            
#sorts the list and prints the sum of the last 3 indexes
print(sum(sorted(totals)[-3:])) 

