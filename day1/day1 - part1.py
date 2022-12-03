lis = []
totals = []


with open("input.txt") as f:
      
    for loop in f.readlines():        # loops through the file and adds 
        if len(loop) > 1:             # every line that isnt empty to a list
            lis.append(int(loop))
              
        else:                         # if a empty line is found the sum of                             
            totals.append(sum(lis))   # the list is added to the "totals" list
            lis = []                  # and then original list is cleared

print(sorted(totals)[-1])   #sorts the list and prints the last index
