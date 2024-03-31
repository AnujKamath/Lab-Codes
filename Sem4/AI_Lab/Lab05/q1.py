class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph={}
        self.minCost=10**8
        self.minPath=[]

    def addEdgeDirected(self, v, w,c):
        print(f"Adding an directed edge between {v} and {w}")
        if w not in self.graph.keys():
            self.graph[w]=[]
        if v in self.graph.keys():
            self.graph[v].append([w,c])
        else:
            self.graph[v]=[[w,c]]
            self.V+=1

    def bfshelp(self,start,goal):
        vis={}
        for c in self.graph.keys():
            vis[c]=False;
        queue=[[0,[start]]]
        self.ucs(queue,vis,goal)

    def ucs(self,queue,vis,goal):
        if len(queue)==0:
            return 
        sorted(queue)
        cost,path=queue.pop(0)# t[0]=cost, t[1]=path, t[1][-1]=last node in that path
        vis[path[-1]]=True
        if goal==path[-1]:
            if self.minCost>cost:
                self.minCost=cost
                self.minPath=path
        if cost>self.minCost:
            return

        for Node,nCost in self.graph[path[-1]]:
            if not vis[Node]:
                path.append(Node)
                queue.append([cost+nCost,path.copy()])# t[0]=prev cost, d[0]=new added cost, t[1]=path
                path.pop()

        self.ucs(queue,vis,goal)

    def printAdjList(self):
        print('\nAdjacency List:')
        for i in self.graph.keys():
            print(f"{i}: ", end = ' [')
            for j in self.graph[i]:
                print(f"{j}", end = ' ')
            print("]")
class q1:
    def main():
        g=Graph(0)
        g.addEdgeDirected('S',1,2)
        g.addEdgeDirected('S',3,5)
        g.addEdgeDirected(3,1,5)
        g.addEdgeDirected(3,4,2)
        g.addEdgeDirected(3,'G',6)
        g.addEdgeDirected(1,'G',1)
        g.addEdgeDirected(2,1,4)
        g.addEdgeDirected('G',4,7)
        g.addEdgeDirected(4,2,4)
        g.addEdgeDirected(4,5,3)
        g.addEdgeDirected(5,'G',3)
        g.addEdgeDirected(5,2,6)


        g.printAdjList()
        s='S'
        goal='G'
        g.bfshelp(s,goal)
        print(f"Minimum Cost from {s} to {goal}= {g.minCost}")
        print(f"Minimum cost from {s} to {goal}= ", end="")
        for c in g.minPath:
            print(c,end=" ")
        print()
    if __name__=="__main__":
        main()