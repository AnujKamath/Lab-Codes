class Stack:
    def __init__(self):
        self.st=[]
    def push1(self,item):
        self.st.append(item)
    def pop1(self):
        if not (self.is_empty()):
            return self.st.pop()
        else:
            print("Stack is empty")
    def is_empty(self):
        return len(self.st)==0
class Queue:
    def __init__(self):
        self.s1=Stack()
        self.s2=Stack()
    def enqueue(self,item):
        self.s1.push1(item)
    def dequeue(self):
        if self.s2.is_empty():
            while not self.s1.is_empty():
                self.s2.push1(self.s1.pop1())
        return self.s2.pop1()
q=Queue()
print("Enter 1 to enqueue, 2 to dequeue, 3 to stop")
n=int(input("Enter choice"))
while n!=3:
    if(n==1):
        x=int(input("Enter a number"))
        q.enqueue(x)
    else:
        x=q.dequeue()
        print(f"Removed element= {x}")
    n=int(input("Enter choice"))


