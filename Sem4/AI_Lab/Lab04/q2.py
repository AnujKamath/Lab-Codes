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

    def bfshelp(self):
        vis={}
        for c in self.graph.keys():
            vis[c]=False;
        queue=[]
        path=[]
        queue.append(1)
        t=list(self.graph.keys())
        self.bfs(queue,path,vis)
        
    def bfs(self,queue,path,vis):
        if len(queue)==0:
            return
        x=queue.pop(0)
        path.append(x)
        vis[x]=True
        for d in self.graph[x]:
            if not vis[d]:
                queue.append(d)
            else:
                print("Cycle found")
                for i in path[::-1]:
                    if i==d:
                        break
                    else:
                        print(f"{i}", end=" ")
                print(d)
        self.bfs(queue,path,vis)
        

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
        g.bfshelp()
    if __name__=="__main__":
        main()
