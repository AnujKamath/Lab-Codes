class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph={}

    def dfshelp(self,n,e):
        vis={}
        for c in self.graph.keys():
            vis[c]=False;
        self.dfs(n,vis,[],e)

    def dfs(self,v,vis,stack,e):
        vis[v]=True
        stack.append(v)
        if(e==v):
            print("Result= ",end="")
            for c in stack:
                print(c,end=" ")
        for d in self.graph[v]:
            if vis[d]==False:
                self.dfs(d,vis,stack,e)
            else:
                x=0
                for d in self.graph[v]:
                    if vis[d]==False:
                        x+=1
                if x==0:
                    if d in stack:
                        stack.pop()
                        while(stack[-1]!=d):
                            stack.pop()


    def printAdjList(self):
        print('\nAdjacency List:')
        for i in self.graph.keys():
            print(f"{i}: ", end = ' [')
            for j in self.graph[i]:
                print(f"{j}", end = ' ')
            print("]")
class q3:
    def main():
        g=Graph(20)
        g.graph={
        1:[2,6],
        2:[1,3],
        3:[2,8],
        4:[5],
        5:[4,10],
        6:[1,11],
        7:[8],
        8:[3,7],
        9:[10,14],
        10:[5,9,15],
        11:[6,12],
        12:[11,17],
        13:[14],
        14:[13,9,19],
        15:[10,20],
        16:[17],
        17:[12,16,18],
        18:[17,19],
        19:[14,18],
        20:[15],
        0:[2,5]
        }
        s=int(input("Enter starting number"))
        e=int(input("Enter ending number"))
        g.printAdjList()
        g.dfshelp(s,e)
    
    if __name__=="__main__":
        main()
