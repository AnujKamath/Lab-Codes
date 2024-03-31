class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.alpha=['A','B','C','D','E']
        self.graph = [[0 for column in range(vertices)]
                            for row in range(vertices)]

    def printAdjMat(self):
        print("\nAdjacency Matrix:")
        for i in range(self.V):
            for j in range(self.V):
                print(f"{self.graph[i][j]}", end = " ")
            print()

    def addEdgeDirected(self, v, w):
        print(f"Adding an directed edge between {self.alpha[v]} and {self.alpha[w]}")
        self.graph[v][w] = 1
        self.graph[w][v] = 1

    def printAdjList(self):
        print('\nAdjacency List:')
        for i in range(self.V):
            print(f"{self.alpha[i]}: ", end = ' [')
            for j in range(self.V):
                if(self.graph[i][j] != 0):
                    print(f"{self.alpha[j]}", end = ',')
            print("]")

class q3:
    def main():
        g = Graph(5)
        g.addEdgeDirected(0,1)
        g.addEdgeDirected(0,2)
        g.addEdgeDirected(0,4)
        g.addEdgeDirected(1,2)
        g.addEdgeDirected(2,4)
        g.addEdgeDirected(2,3)
        g.printAdjList()
        g.printAdjMat()
    if __name__=="__main__":
        main()