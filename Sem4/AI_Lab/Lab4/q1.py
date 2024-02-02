class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph={}
        self.indegree={}

    def addEdgeDirected(self, v, w):
        print(f"Adding an directed edge between {v} and {w}")
        if w not in self.graph.keys():
            self.graph[w]=[]
        if v in self.graph.keys():
            self.graph[v].append(w)
        else:
            self.graph[v]=[w]
            self.V+=1
        if w not in self.indegree.keys():
            self.indegree[w]=0
        if v not in self.indegree.keys():
            self.indegree[v]=0
        self.indegree[w]+=1
        

    def topsort(self):
        vis={}
        for c in self.graph.keys():
            vis[c]=False
        queue=[]
        path=[]
        for d,value in self.indegree.items():
            if value==0:
                queue.append(d)
        self.dfs(vis,queue,path)
        return path

    def dfs(self,vis,queue,path):
        if len(queue)>0:
            t=queue.pop(0)
            path.append(t)
            vis[t]=True
            for d in self.graph[t]:
                if not vis[d]:
                    self.indegree[d]-=1
                    if self.indegree[d]==0:
                        queue.append(d)
                        self.indegree[d]=-1
            self.dfs(vis,queue,path)


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
