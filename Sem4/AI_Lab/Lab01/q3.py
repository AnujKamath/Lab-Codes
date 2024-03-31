x=[[1,2],[3,4],[5,6]]
y=[[9,8],[4,2],[7,0]]
def dist():
    global x,y
    ans=[]
    for i in range(0,len(x)):
        d=pow((y[i][0]-x[i][0])**2+(y[i][1]-x[i][1])**2,0.5)
        ans.append(d)
    return ans
def bsort(ans):
    for i in range(0,len(ans)-1):
        for j in range(0,len(ans)-1-i):
            if ans[j]>ans[j+1]:
                t=ans[j]
                ans[j]=ans[j+1]
                ans[j+1]=t
    return ans

ans=dist()
ans=bsort(ans)
print(ans)

