f = open("4.txt", "r")

inp = f.read().split("\n")
total=0
for each in inp:
    pairs = each.split(",")
    fir = pairs[0].split("-")
    sec = pairs[1].split("-")
    # if int(fir[0])>=int(sec[0]) and int(fir[1])<=int(sec[1]):
    #     total+=1
    # elif int(fir[0])<=int(sec[0]) and int(fir[1])>=int(sec[1]):
    #     total+=1
    if int(fir[1])>=int(sec[0]) and int(sec[1])>=int(fir[0]):
        total+=1
print(total)