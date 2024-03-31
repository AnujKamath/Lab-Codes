class Graph:
    def __init__(self):
        self.edges = {}
        self.heu = {}
    def addNodes(self, nodes):       
        for node in nodes:
            self.edges[node] = {}
    def addEdge(self, node1, node2, weight = 1):
        self.edges[node1][node2] = weight
    def printList(self):
        for node, sub in self.edges.items():
            print(f"Node {node}: ", end = ' ')
            for neighbor, weight in sub.items():
                print(f"{neighbor}:{weight}     ", end='')
            print()
    def aStar(self, start, end):
        q = [(self.heu[start], start, [start], 0)]  # [heucost, node, [path], cost]        
        while q:
            curr_node = q.pop(0)
            if(curr_node[1] == end):
                return curr_node
            for neighbor in self.edges[curr_node[1]]:
                if neighbor not in curr_node[2]:
                    q.append((curr_node[3] + self.heu[neighbor] + self.edges[curr_node[1]][neighbor],
                               neighbor,
                                 curr_node[2] + [neighbor],
                                  curr_node[3] + self.edges[curr_node[1]][neighbor]))
                    q.sort()

g = Graph()
g.addNodes(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
g.edges = {
    'A': {'B':6, 'F':3},
    'B': {'A':6, 'C':3, 'D':2},
    'C': {'E':5, 'D':1, 'B':3},
    'D': {'B':2, 'C':1, 'E':8},
    'E': {'C':5, 'D':8, 'I':5, 'J':5},
    'F': {'A':3, 'G':1, 'H':7},
    'G': {'F':1, 'I':3},
    'H': {'F':7, 'I':2},
    'I': {'E':5, 'G':3, 'H':2, 'J':3},
    'J': {'E':5, 'I':3}
}
g.heu = {
    'A':10,
    'B':8,
    'C':5,
    'D':7,
    'E':3,
    'F':6,
    'G':5,
    'H':3,
    'I':1,
    'J':0
}

curr_node = g.aStar('A', 'J')
print(f"Path:{curr_node[2]} \nCost: {curr_node[3]}\n")
