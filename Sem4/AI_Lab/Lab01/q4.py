class Node:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.data = v
root=Node(25)
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.data,end=" ")
        printInorder(root.right)
def printPreOrder(node):
    if node is None:
        return
    print(node.data, end = " ")
    printPreOrder(node.left)
    printPreOrder(node.right)

def printPostOrder(node):
    if node is None:
        return
    printPostOrder(node.left)
    printPostOrder(node.right)
    print(node.data, end = " ")
def createBST(i):
    global root
    node =root
    while(True):
        if node.data<i:
            if node.right==None:
                 node.right=Node(i)
                 break
            else:
                 node=node.right
        else:
            if node.left==None:
                 node.left=Node(i)
                 break
            else:
                 node=node.left
             
                       
 
if __name__ == "__main__":
    t=[15,50,10,22,35,70,4,12,18,24,31,44,66,90]
    for i in t:
        createBST(i)
    print("Inorder Traversal:",end=" ")
    printInorder(root)
    print()
    print("Preorder Traversal: ", end = "")
    printPreOrder(root)
    print()
    print("Postorder Traversal: ", end = "")
    printPostOrder(root)
    print()