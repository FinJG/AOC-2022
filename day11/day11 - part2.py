import re
dic = {}
lis = []
commonmultiple = 1
with open("input.txt") as file:
    f = file.read().strip().splitlines()
    for line in f:
        if line.startswith("Monkey"):
            ind = int(re.findall("\d+", line)[0])
            lis.append([])
        if line.startswith("  Starting"):
            for num in re.findall("\d+", line):
                lis[ind].append(num)   
        if line.startswith("  Test"):
            divisor = re.findall("\d+", line)
            commonmultiple *= int(divisor[0])
 

def monkeypass(lis, commonmultiple):
    for line in f:
        if line.startswith("Monkey"):
            ind = int(re.findall("\d+", line)[0])

        if line.startswith("  Operation"):
            operation = re.findall("=.+", line)[0][2:].split()
            num1 = operation[0]
            num2 = operation[2]
            operator = operation[1]
        
            for i, loop in enumerate(lis[ind]):
                if num1 == "old":
                    no1 = loop
                else:
                    no1 = num1
                if num2 == "old":
                    no2 = loop
                else:
                    no2 = num2
                if operator == "*":
                    lis[ind][i] = int(no1) * int(no2)
                else:
                    lis[ind][i] = int(no1) + int(no2)
                    pass
        if line.startswith("  Test"):
            divisor = re.findall("\d+", line)
        if line.startswith("    If true"):
            choice1 = int(re.findall("\d+", line)[0])
        if line.startswith("    If false"):
            choice2 = int(re.findall("\d+", line)[0])



            for i, num in enumerate(lis[ind]):
                if not ind in dic.keys():
                    dic[ind] = 1
                else:
                    dic[ind] += 1
                multiple = int(num) % commonmultiple
                lis[ind][i] = multiple
                if multiple % int(divisor[0]) == 0:
                    lis[choice1].append(multiple)
                else:
                    lis[choice2].append(multiple)
                lis[ind][i] = "w"
    
            lis = [[i for i in x if i != "w"] for x in lis]
    return lis, commonmultiple

        
c = 0

for x in range(10000):
    lis, commonmultiple = monkeypass(lis, commonmultiple)
    c += 1 
    mostpass = sorted([i for i in dic.values()])[-2:]
print(mostpass[0] * mostpass[1])