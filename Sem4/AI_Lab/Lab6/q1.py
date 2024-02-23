import random 
import math
class q1:
    def __init__(self,l,u):
        self.lower=l
        self.upper=u
        self.maxa=-1
    def f(self,x):
        return x**3+x**2
    
    def gen_neighbours(self,x):
        return max(self.lower,x-0.1),min(self.upper,x+0.1)
    
    def hcs(self,iters=50):
        for i in range(iters):
            x=random.randint(self.lower,self.upper)
            while True:
                x1,x2=self.gen_neighbours(x)
                max_x=max(self.f(x1), self.f(x), self.f(x2))
                if max_x==self.f(x):
                    self.maxa=round(max(self.f(x),self.maxa),3)
                    break
                if max_x==self.f(x2):
                    x=x2
                else:
                    x=x1
q=q1(-10,10)
q.hcs(50)
print(f"The maximum value obtained is={q.maxa}")
