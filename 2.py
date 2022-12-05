
# import requests
# URL = "https://adventofcode.com/2022/day/1/input"
# r = requests.get(url=URL)
# data = r.json()
f = open("2.txt", "r")

bags = f.read().split("\n")

score = {"A X": 4,
"A Y": 8, 
"A Z": 3,
"B X": 1,
"B Y": 5,
"B Z": 9,
"C X": 7,
"C Y": 2,
"C Z": 6}
score2 = {"A X": 3,
"A Y": 4, 
"A Z": 8,
"B X": 1,
"B Y": 5,
"B Z": 9,
"C X": 2,
"C Y": 6,
"C Z": 7}
total = 0
print(bags)
for each in bags:
    try:
        total+=score2[each]
    except:
        pass
print(total)
