class Graph:
    def __init__(self):
        self.edges = {}
        self.heu = {}
        self.minic=999999999
        self.minipath=[]  
    def addNodes(self, nodes):
        for node in nodes:
            self.edges[node] = {}
    def aStar(self, start, end):
        q = [(self.heu[start], start, [start], 0)]  # [heucost, node, [path], cost]     
        while q:
            q.sort(key = lambda x: x[0])
            curr_node = q.pop(0)
            if curr_node[3]>self.minic:
                return
            if curr_node[1] in end:
                if self.minic>curr_node[3]:
                    self.minic=curr_node[3]
                    self.minipath=curr_node[2]
            for neighbor in self.edges[curr_node[1]]:
                if neighbor not in curr_node[2]:
                    q.append((curr_node[3] + self.heu[neighbor] + self.edges[curr_node[1]][neighbor],
                              neighbor,
                              curr_node[2] + [neighbor],
                              curr_node[3] + self.edges[curr_node[1]][neighbor])) 
        
g = Graph()
g.addNodes(['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G1', 'G2', 'G3'])
g.edges = {
    'S': {'A':5, 'B':9, 'D':6},
    'A': {'G1':9, 'B':3},
    'B': {'A':2, 'C':1, },
    'C': {'G2':5, 'S':6, 'F':7},
    'D': {'C':2, 'E':2, 'S':1},
    'E': {'G3':7},
    'F': {'D':2, 'G3':8},
    'G1': {},
    'G2': {},
    'G3': {}
}
g.heu = {
    'S':5,
    'A':7,
    'B':3,
    'C':4,
    'D':6,
    'E':5,
    'F':6,
    'G1':0,
    'G2':0,
    'G3':0
}
end=['G1','G2','G3']
g.aStar('S', end)
print(f"Path= {g.minipath}\nCost= {g.minic}\n")
