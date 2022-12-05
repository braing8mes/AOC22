
# import requests
# URL = "https://adventofcode.com/2022/day/1/input"
# r = requests.get(url=URL)
# data = r.json()
f = open("1.txt", "r")

bags = f.read().split("\n\n")

max = [0, 0, 0]
for each in bags:
    nums = each.split("\n")
    total = 0
    for num in nums:
        total+=int(num)
    if total>max[2]:
        if total>max[1]:
            if total>max[0]:
                max = [total]+max[1:]
            else:
                max = [max[0], total, max[2]]
        else:
            max = max[:2]+[total]
for i in range(len(bags)):
    nums = bags[i].split("\n")
    total = 0
    for num in nums:
        total+=int(num)
    bags[i] = total

print(sum(sorted(bags, reverse=True)[:3]))