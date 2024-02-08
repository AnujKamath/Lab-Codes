class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph={}
    def bfshelp(self):
        vis={}
        t=list(self.graph.keys())
        for c in t:
            vis[c]=False
        queue=[]
        pusher=[t[0]]
        queue.append(t[0])
        self.bfs(queue,pusher,vis)
        return pusher
        
    def bfs(self,queue,pusher,vis):
        if len(queue)==0:
            return
        x=queue.pop(0)
        vis[x]=True
        for d in self.graph[x]:
            if not vis[d]:
                queue.append(d)
                if d not in pusher:
                    pusher.append(d)
        self.bfs(queue,pusher,vis)
        

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
        g.graph={ 'A': ['B','C','D'],
                  'B': ['A','C','D'],
                  'C': ['A', 'B', 'D'],
                  'D': ['A', 'B', 'C']}
        g.printAdjList()
        pusher=g.bfshelp()
        print("Traversal Order :",end="")
        for t in pusher:
            print(t,end=" ")
        print()
    if __name__=="__main__":
        main()
