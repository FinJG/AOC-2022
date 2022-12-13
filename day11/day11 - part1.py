from re import findall
dic = {}
with open("input.txt") as file:
    f = file.read().strip().splitlines()
    for line in f:
        if line.startswith("Monkey"):
            ind = int(findall("\d+", line)[0])
            dic[ind] = {"count":0, "values":[], "test":0, "true":0, "false":0}
        if line.startswith("  Starting"):
            for num in findall("\d+", line):
                dic[ind]["values"].append(int(num)) 
        if line.startswith("  Test"):
            dic[ind]["test"] = int(findall("\d+", line)[0])
        if line.startswith("    If true"):
            dic[ind]["true"] = int(findall("\d+", line)[0])
        if line.startswith("    If false"):
            dic[ind]["false"] = int(findall("\d+", line)[0])

def monkeypass():
    for line in f:
        if line.startswith("Monkey"):
            ind = int(findall("\d+", line)[0])
        if line.startswith("  Operation"):
            operator, num2 = findall("=.+", line)[0][2:].split()[1:]
            for i, loop in enumerate(dic[ind]["values"]):
                if num2 == "old":
                    no2 = loop
                else:
                    no2 = int(num2)
                if operator == "*":
                    dic[ind]["values"][i] = loop * no2
                else:
                    dic[ind]["values"][i] = loop + no2

            for i, num in enumerate(dic[ind]["values"]):
                multiple = num//3
                if (multiple / dic[ind]["test"]).is_integer():
                    dic[dic[ind]["true"]]["values"].append(multiple)
                else:
                    dic[dic[ind]["false"]]["values"].append(multiple)

                dic[ind]["count"] += 1  
                dic[ind]["values"][i] = "x"
            for loop in dic.keys():
                dic[loop]["values"] = [i for i in dic[loop]["values"] if i != "x"]

for loop in range(20):
    monkeypass()

mostpass = sorted([i for i in [dic[key]["count"] for key in dic.keys()]])[-2:]
print(mostpass[0] * mostpass[1])
