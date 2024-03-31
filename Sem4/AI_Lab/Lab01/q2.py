class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                            for row in range(vertices)]

    def printAdjMat(self):
        print("\nAdjacency Matrix:")
        for i in range(self.V):
            for j in range(self.V):
                print(f"{self.graph[i][j]}", end = " ")
            print()

    def addEdgeDirected(self, v, w, weight):
        print(f"Adding an directed edge between {v+1} and {w+1}")
        self.graph[v][w] = weight

    def printAdjList(self):
        c = 0
        print('\nAdjacency List:')
        for row in self.graph:
            print(f"{c+1}: ", end = '  ')
            for index,val in enumerate(row):
                if(val != 0):
                    print(f"[{index + 1},{val}]", end = ' ')
            c+=1
            print()

g = Graph(4)
g.addEdgeDirected(0,1,1)
g.addEdgeDirected(1,2,3)
g.addEdgeDirected(2,3,4)
g.addEdgeDirected(3,0,5)
g.addEdgeDirected(0,2,1)


g.printAdjMat()
g.printAdjList()