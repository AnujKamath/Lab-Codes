#include <stdio.h>
#include <stdlib.h>
typedef struct Node{
    int v;
    struct Node* l;
    struct Node* r;
} Node;
Node* create(int x)
{
    Node* temp=(Node*)malloc(sizeof(Node));
    temp->v=x;
    temp->l=NULL;
    temp->r=NULL;
    return temp;
}
void check(Node* root,int x)
{
    if(!root)
    {
        root=create(x);
        return;}
    Node* tree=root;
    Node* par=root;
    while(tree)
    {
        if(tree->v==x)
        {
            printf("Key Found");
        return;
        }
        else if(tree->v>x)
        {
            par=tree;
            tree=tree->l;
        }
        else
        {
            par=tree;
            tree=tree->r;
        }
    }
    if(par&&!tree)
    {
        if(par->v>x)
        par->l=create(x);
        else
        par->r=create(x);
    }      
}
void inorder(Node* tree)
{
    if(tree)
    {
        inorder(tree->l);
        printf("%d",tree->v);
        inorder(tree->r);
    }
}
void postorder(Node* tree)
{
    if(tree)
    {
        postorder(tree->l);
        postorder(tree->r);
        printf("%d",tree->v);
    }
}
void preorder(Node* tree)
{
    if(tree)
    {
        printf("%d",tree->v);
        preorder(tree->l);
        preorder(tree->r);
    }
}
int main()
{
    Node* root=NULL;
    int n=1;
    printf("Enter 1 to search for a value, 2 to print traversals, 3 to stop");
    printf("Enter choice");
    scanf("%d",&n);
    while(n!=3)
    {
        if(n==1)
        {
            printf("Enter value");
            int x;
            scanf("%d",&x);
            if(!root)
            root=create(x);
            else
            check(root,x);
        }
        else if(n==2)
        {
            printf("Enter 1 for preorder, 2 for inorder or 3 for postorder");
            int c;
            scanf("%d",&c);
            if(c==1)
            preorder(root);
            else if(c==2)
            inorder(root);
            else
            postorder(root);
        }
        printf("Enter choice");
        scanf("%d",&n);         
    }
    return 0;
}
