import math
f = open("10.txt","r")
inp = f.read().split("\n")
reg = [1]
curr = 1
for each in inp:
    if each == 'noop':
        reg.append(curr)
    elif each.startswith("addx"):
        value = each.split()[-1]
        reg.extend([curr, curr])
        curr += int(value)
total = 0
last = math.floor(len(reg)/40)
cycles = [20+40*x for x in range(last)]
for num in cycles:
    total+= num*reg[num]
print(reg)
print(total)