class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                            for row in range(vertices)]
    def addEdgeDirected(self, v, w, weight):
        print(f"Adding an directed edge between {v} and {w}")
        self.graph[v][w] = weight

    def printAdjList(self):
        c = 0
        print('\nAdjacency List:')
        for i in range(self.V):
            for j in range(self.V):
                if(self.graph[i][j] != 0):
                    print(f"({i}->{j},{self.graph[i][j]})", end = ' ')
            print()

class q2:
    def main():
        g = Graph(6)
        g.addEdgeDirected(0,1,6)
        g.addEdgeDirected(1,2,7)
        g.addEdgeDirected(2,0,5)
        g.addEdgeDirected(2,1,4)
        g.addEdgeDirected(3,2,10)
        g.addEdgeDirected(4,5,1)
        g.addEdgeDirected(5,4,3)
        g.printAdjList()
    if __name__=="__main__":
        main()