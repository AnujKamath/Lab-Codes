class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph={}

    def addEdgeDirected(self, v, w):
        print(f"Adding an directed edge between {v} and {w}")
        if w not in self.graph.keys():
            self.graph[w]=[]
        if v in self.graph.keys():
            self.graph[v].append(w)
        else:
            self.graph[v]=[w]
            self.V+=1

    def dfshelp(self):
        vis={}
        for c in self.graph.keys():
            vis[c]=False;
        stack=[]
        t=list(self.graph.keys())
        for d in t[::-1]:
            if not vis[d]:
                # print(f"&{d}&")
                self.dfs(d,vis,stack)
        return stack[::-1]

    def dfs(self,v,vis,stack):
        vis[v]=True
        stack.append(v)
        # print(stack)
        for d in self.graph[v]:
            if vis[d]:
                print("Cycle found:",end=" ")
                for c in stack[::-1]:
                    if d==c:
                        print(c,end=" ")
                        # print(stack)
                        break;
                    else:
                        print(c,end=" ")
                print()
            else:
                # print(d)
                self.dfs(d,vis,stack)
                # vis[stack[-1]]=False
                # stack.pop()


    def printAdjList(self):
        print('\nAdjacency List:')
        for i in self.graph.keys():
            print(f"{i}: ", end = ' [')
            for j in self.graph[i]:
                print(f"{j}", end = ' ')
            print("]")
class q2:
    def main():
        g=Graph(0)
        g.addEdgeDirected(2,0)
        g.addEdgeDirected(2,3)
        g.addEdgeDirected(0,2)
        g.addEdgeDirected(0,1)
        g.addEdgeDirected(1,2)
        g.addEdgeDirected(3,3)

        g.printAdjList()
        st=g.dfshelp()
        print("Result= ",end="")
        for c in st:
            print(c,end=" ")
    if __name__=="__main__":
        main()