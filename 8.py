import numpy as np
f = open("8.txt","r")
inp = f.read().split("\n")
nrows = len(inp)
ncols = len(inp[0])
t = []
heh = np.zeros(shape=(nrows,ncols))
for each in inp:
    t.append([int(i) for i in list(each)])
trees = np.array(t)
for i in range(nrows):
    for j in range(ncols):
        if trees[i][j]<trees[i][j+1]:
            # print("reached here with "+str(i)+str(j))
            heh[i][j+1] = 1
        elif trees[i][j] == trees[i][j+1]:
            continue
        else:
            break
for i in range(nrows):
    for j in range(ncols):
        if trees[i][ncols-2-j]>trees[i][ncols-j-1]:
            heh[i][ncols-j-2] = 1
        elif trees[i][ncols-2-j] == trees[i][ncols-j-1]:
            continue
        else:
            break
for j in range(ncols):
    for i in range(nrows):
        if trees[i][j]<trees[i+1][j]:
            heh[i+1][j] = 1
        elif trees[i][j] == trees[i+1][j]:
            continue
        else:
            break
for i in range(nrows):
    for j in range(ncols):
        if trees[nrows-i-2][j]>trees[nrows-i-1][j]:
            heh[nrows-i-2][j] = 1
        elif trees[nrows-i-2][j] == trees[nrows-i-1][j]:
            continue
        else:
            break
for j in range(ncols):
    heh[0][j] = 1
    heh[nrows-1][j] = 1
for i in range(nrows):
    heh[i][0] = 1
    heh[i][ncols-1] = 1
print(heh)
print(str(nrows)+" " +str(ncols))
print(np.count_nonzero(heh))