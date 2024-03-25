class Wumpus:
    def __init__(self):
        self.grid=[['s',' ',' ',' '],
                   ['W','s','G',' '],
                   ['s',' ','B',' '],
                   ['A','B','P','B']]
        self.size=4
        self.agent_pos=(3,0)
        self.vis=[['N' for _ in range(4)]for _ in range(4)]
        self.path=[]
        self.minpath=[]
    def move(self):
        x,y=self.agent_pos
        poss=[]
        if y>0:
            poss.append([x,y-1])
        if y<self.size-1:
            poss.append([x,y+1])
        if x>0:
            poss.append([x-1,y])
        if x<self.size-1:
            poss.append([x+1,y])
        i=0
        while(i<len(poss)):
            c = self.grid[poss[i][0]][poss[i][1]]
            if c == 'W' or c == 'P':
                poss.pop(i)
                i=i-1
            i+=1

        return poss
    def traverse(self,vis):
        x,y=self.agent_pos
        if self.grid[x][y]=='G':
            print("Found gold")
            self.path.append([x,y])
            print(self.path)
            print(vis)
            exit(1)

        if vis[x][y]!='N':
            return
        print("Agent at=",self.agent_pos)
        vis[x][y]='Y'
        if self.grid[x][y]=='B':
            for d in self.move():
                c=self.vis[d[0]][d[1]]
                if c=='N':
                    vis[d[0]][d[1]]='P1'
                elif c=='W1':
                    vis[d[0]][d[1]]='N'
            vis[x][y]='B'
            print(f"Found breeze at {x},{y}")


        if self.grid[x][y]=='s':
            for d in self.move():
                c=vis[d[0]][d[1]]
                if c=='N':
                    vis[d[0]][d[1]]='W1'
                elif c=='P1':
                    vis[d[0]][d[1]]='N'
            vis[x][y]='s'
            print(f"Found stench at {x},{y}")

        if self.grid[x][y]==' ' or self.grid[x][y]=='G':
            for d in self.move():
                c=vis[d[0]][d[1]]
                if c=='P1' or c=='W1':
                        vis[d[0]][d[1]]='N'
        for d in self.move():
            if vis[d[0]][d[1]]=='N':
                self.agent_pos=d
                c=self.path.copy()
                v1=vis.copy()
                self.path.append([x,y])
                self.traverse(v1)
                self.path=c
g=Wumpus()
g.traverse(g.vis)
