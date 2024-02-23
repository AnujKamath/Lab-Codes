def error(curr,goal):
    temp=0
    for i in range(len(curr)):
        for j in range(len(curr)):
            if curr[i][j]!=goal[i][j]:
                temp+=1
    return temp
def check_bound(n,x,y):
    if x>=n or x<0 or y>=n or y<0:
        return False
    return True
def gen_neighbours(curr):
    next_x=[1,-1,0,0]
    next_y=[0,0,1,-1]
def hcs(start,goal,iters=50):
