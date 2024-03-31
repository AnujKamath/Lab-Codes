class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[0 for column in range(vertices)]
                            for row in range(vertices)]
    def addEdgeDirected(self, v, w):
        print(f"Adding an directed edge between {v} and {w}")
        self.graph[v][w] = 1

    def printAdjList(self):
        c = 0
        for i in range(self.v):
            for j in range(self.v):
                if(self.graph[i][j] != 0):
                    print(f"({i}->{j})", end = ' ')
            print()

class q1:
    def main():
        g = Graph(6)
        g.addEdgeDirected(0,1)
        g.addEdgeDirected(1,2)
        g.addEdgeDirected(2,0)
        g.addEdgeDirected(2,1)
        g.addEdgeDirected(3,2)
        g.addEdgeDirected(4,5)
        g.addEdgeDirected(5,4)
        g.printAdjList()
    if __name__=="__main__":
        main()
