import random

def misplaced(mat, ans):
    count = 0
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] != ans[i][j]:
                count += 1
    return count

def find(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if(mat[i][j] == 0):
                return i,j

def genchild(mat):
    x,y = find(mat)
    val = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]
    children = []
    for elem in val:
        if (len(mat) > elem[0] >= 0 and len(mat) > elem[1] >= 0):
            temp = [row[:] for row in mat]
            a=temp[x][y]
            temp[x][y] = temp[elem[0]][elem[1]]
            temp[elem[0]][elem[1]]=a
            children.append(temp)
    return children

def hcs(start, end, iter = 1000):
    minpath = []
    k=0
    for i in range(iter):
        mat = start if len(minpath) == 0 else minpath.pop()
        minpath.append(mat)
        children = genchild(mat)
        while True:
            vals = []
            for child in children:
                vals.append((misplaced(child, end), child))
            random.shuffle(vals)
            h=0
            for i in range(len(vals)):
                if(vals[i][1] not in minpath) and vals[i][0]<=misplaced(mat,end):
                    minpath.append(vals[i][1])
                    h=vals[i][0]
                    break
            if h==0:
                break
            if misplaced(minpath[-1], end) == 0:
                break
        if misplaced(minpath[-1], end) == 0:
                break
    return minpath


mat = [[1,2,3], [0,4,6], [7,5,8]]
ans = [[1,2,3], [4,5,6], [7,8,0]]
process=hcs(mat, ans, 10)
for i in range(len(process)):
    for j in range(3):
        for k in range(3):
            print(f" {process[i][j][k]} ",end="")
    if(i!=len(process)-1):
        print("")
        print("  | ")
        print("  | ")
        print(" \\\'/ \n")
# for i in range(3):
#     for j in range(3):
#         print(f" {process[-1][i][j]} ",end="")
