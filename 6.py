f = open("6.txt", "r")
inp = f.read()
assert type(inp)==str
for i in range(len(inp)):
    # if len(set(inp[i:i+4])) == 4:
    #     print(i+4)
    #     break
    if len(set(inp[i:i+14])) == 14:
        print(i+14)
        break