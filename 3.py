


f = open("3.txt", "r")

bags = f.read().split("\n")
total = 0
"""for string in bags:
    fir, sec = string[:len(string)//2], string[len(string)//2:]
    prio = set(fir).intersection(set(sec))
    letter = "".join(prio)
    print(letter)
    if letter.isupper():
        total+=ord(letter)-38
    else:
        total+=ord(letter) - 96"""

print(total)
