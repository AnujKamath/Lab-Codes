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

    def topsort(self):
        vis={}
        for c in self.graph.keys():
            vis[c]=False;
        stack=[]
        for d in self.graph.keys():
            if not vis[d]:
                self.dfs(d,vis,stack)
        return stack[::-1]

    def dfs(self,v,vis,stack):
        vis[v]=True
        for d in self.graph[v]:
            if not vis[d]:
                self.dfs(d,vis,stack)
        stack.append(v)


    def printAdjList(self):
        print('\nAdjacency List:')
        for i in self.graph.keys():
            print(f"{i}: ", end = ' [')
            for j in self.graph[i]:
                print(f"{j}", end = ' ')
            print("]")
# 523104
class q1:
    def main():
        g=Graph(0)
        g.addEdgeDirected(5,0)
        g.addEdgeDirected(5,2)
        g.addEdgeDirected(4,0)
        g.addEdgeDirected(4,1)
        g.addEdgeDirected(3,1)
        g.addEdgeDirected(2,3)
        g.printAdjList()
        st=g.topsort()
        print("Result= ",end="")
        for c in st:
            print(c,end=" ")
    if __name__=="__main__":
        main()