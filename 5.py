
# import requests
# URL = "https://adventofcode.com/2022/day/1/input"
# r = requests.get(url=URL)
# data = r.json()
import queue

f = open("3.txt", "r")
q1 = ["j", "h", "p", "m","s","f","n","v"]
q2 = list("srlmjdq")
q3 = list("nqdhcswb")
q4 = list("rscl")
q5 = list("mvtpfb")
q6 = list("trqnc")
q7 = list("gvr")
q8 = list("czspdlr")
q9 = list("dsjvgpbf")
my_dict = {
1:q1,
2:q2,
3:q3,
4:q4,
5:q5,
6:q6,
7:q7,
8:q8,
9:q9
}

x = f.read().split("\n")[10:]
for each in x:
    # words = each.split()
    # for i in range(int(words[1])):
    #     temp = my_dict[int(words[3])].pop()
    #     my_dict[int(words[5])].append(temp)
    #     for each in x:
    words = each.split()
    num = int(words[1])
    old = my_dict[int(words[3])].copy()
    new = my_dict[int(words[5])].copy()
    move = old[-1*num:]
    left = old[:-1*num]
    my_dict[int(words[5])].extend(move)
    my_dict[int(words[3])] = left
print(my_dict)

