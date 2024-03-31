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
class q1:
    def main():
        g=Graph(0)
        g.addEdgeDirected('Dunwich', 'Blaxhall', 17)
        g.addEdgeDirected('Blaxhall', 'Dunwich', 15)
        g.addEdgeDirected('Harwich', 'Dunwich', 53)
        g.addEdgeDirected('Harwich', 'Blaxhall', 40)
        g.addEdgeDirected('Feering', 'Blaxhall', 46)
        g.addEdgeDirected('Tiptree', 'Feering', 3)
        g.addEdgeDirected('Harwich', 'Tiptree', 31)
        g.addEdgeDirected('Clacton', 'Harwich', 17)
        g.addEdgeDirected('Tiptree', 'Clacton', 29)
        g.addEdgeDirected('Feering', 'Maldon', 11)
        g.addEdgeDirected('Maldon', 'Tiptree', 8)
        g.addEdgeDirected('Clacton', 'Maldon', 40)


        g.printAdjList()
        s='Maldon'
        goal='Dunwich'
        g.bfshelp(s,goal)
        print(f"Minimum Cost from {s} to {goal}= {g.minCost}")
        print(f"Minimum cost from {s} to {goal}= ", end="")
        for c in g.minPath:
            print(c,end=" ")
        print()
    if __name__=="__main__":
        main()