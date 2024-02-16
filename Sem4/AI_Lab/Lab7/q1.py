def astar(start,stop):
    open=set(start)
    closed=set()
    g={}
    parents={}

    g[start]=0
    parents[start]=start
    while len(open)>0:
        n=None
        for v in open:
            if n==None or g[v]+heuristic(v)<g[n]+heuristic(n):
                n=v
        if n==stop or Graph[n]==None:
            pass
        else:
            for (m,w) in get_neighbours(n):
                if m not in open and m not in closed:
                    open.add(m)
                    parents[m]=n
                    g[m]=g[n]+w
                else:
                    if g[m]>g[n]+w:
                        g[m]=g[n]+w
                        parents[m]=n
                        if m in closed:
                            closed.remove(m)
                            open.add(m)
        if n==None:
            print("path not there")
            return None
        if n==stop:
            path=[]
            while parents[n]!=n:
                path.append(n)
                n=parents[n]
            path.append(start)
            path.reverse()
            print('Path found:{}'.format(path))
            return path
        open.remove(n)
        closed.add(n)
    print('path not exist')
    return None
def get_neighbours(v):
    return Graph[v]
def heuristic(n):
    h_dist={'A':10,'B':8,'C':5,'D':7,'E':3,'F':6,'G':5,'H':3,'I':1,'J':0}
    return h_dist[n]
Graph={'A':[('B',6),('F',3)],
       'B':[('c',3),('D',2)],
       'c':None,
       'e':[('d',6)],
       'd':[('g',1)]}
astar('A','J')
