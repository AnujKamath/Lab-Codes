class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph={}
        self.minCost=10**8
        self.minPath=[]

    def addEdgeDirected(self, v, w,c):
        # print(f"Adding an directed edge between {v} and {w}")
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
class q2:
    def main():
        g=Graph(0)
        g.addEdgeDirected('S', 'A', 5)
        g.addEdgeDirected('S', 'B', 9)
        g.addEdgeDirected('C', 'S', 6)
        g.addEdgeDirected('S', 'D', 6)
        g.addEdgeDirected('A', 'B', 3)
        g.addEdgeDirected('B', 'A', 3)
        g.addEdgeDirected('B', 'C', 1)
        g.addEdgeDirected('D', 'C', 2)
        g.addEdgeDirected('D', 'E', 2)
        g.addEdgeDirected('E', 'G3', 7)
        g.addEdgeDirected('F', 'G3', 8)
        g.addEdgeDirected('F', 'D', 2)
        g.addEdgeDirected('C', 'F', 7)
        g.addEdgeDirected('C', 'G2', 5)
        g.addEdgeDirected('A', 'G1', 9)


        # g.printAdjList()
        goal = ['G1', 'G2', 'G3']
        mc=10**8
        mp=[]
        for node in goal:
            g.bfshelp('S',node)
            if g.minCost<mc:
                mc=g.minCost
                mp=g.minPath
            g.minCost=10**8
            g.minPath=[]
        print(f"Minimum Cost from S to goal node= {mc}")
        print(f"Minimum cost Path from S to goal node= ", end="")
        for c in mp:
            print(c,end=" ")
        print()
        
    if __name__=="__main__":
        main()