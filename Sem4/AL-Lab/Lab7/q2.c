#include <stdio.h>
#include <stdlib.h>

#define MAX_NODES 100
int z=0;
int q=0;
typedef struct Node
{
    int data;
    struct Node *l;
    struct Node *r;
    int height;
} Node;

Node *stack[MAX_NODES];
int top = -1;

Node *peek()
{
    if (top == -1)
        return NULL;
    return stack[top];
}

void push(Node *node)
{
    if (top == MAX_NODES - 1)
        return;
    stack[++top] = node;
}

Node *pop()
{
    if (top == -1)
        return NULL;
    return stack[top--];
}

int max(int a, int b)
{
    return (a > b) ? a : b;
}

int height(Node *node)
{
    if (node == NULL)
        return 0;
    return node->height;
}

Node *newNode(int data)
{
    Node *node = (Node *)malloc(sizeof(Node));
    node->data = data;
    node->l = NULL;
    node->r = NULL;
    node->height = 1;
    return node;
}

Node *rRotate(Node *y)
{
    Node *x = y->l;
    Node *T2 = x->r;

    x->r = y;
    y->l = T2;

    y->height = max(height(y->l), height(y->r)) + 1;
    x->height = max(height(x->l), height(x->r)) + 1;

    return x;
}

Node *lRotate(Node *x)
{
    Node *y = x->r;
    Node *T2 = y->l;

    y->l = x;
    x->r = T2;

    x->height = max(height(x->l), height(x->r)) + 1;
    y->height = max(height(y->l), height(y->r)) + 1;

    return y;
}

int diffbal(Node *node)
{
    if (node == NULL)
        return 0;
    return height(node->l) - height(node->r);
}

Node *insertNode(Node *root, int data)
{
    Node *new_node = newNode(data);
    if (root == NULL)
        return new_node;

    Node *cur = root;

    while (cur != NULL)
    {
        push(cur);
        if (data < cur->data)
            cur = cur->l;
        else if (data > cur->data)
            cur = cur->r;
        else
        {
            free(new_node);
            return root;
        }
    }

    Node *par = peek();
    if (data < par->data)
        par->l = new_node;
    else
        par->r = new_node;

    while (top != -1)
    {
        cur = pop();
        cur->height = 1 + max(height(cur->l), height(cur->r));
        int balance = diffbal(cur);

        if (balance > 1 && data < cur->l->data)
            cur = rRotate(cur);
        else if (balance < -1 && data > cur->r->data)
            cur = lRotate(cur);
        else if (balance > 1 && data > cur->l->data)
        {
            cur->l = lRotate(cur->l);
            cur = rRotate(cur);
        }
        else if (balance < -1 && data < cur->r->data)
        {
            cur->r = rRotate(cur->r);
            cur = lRotate(cur);
        }

        if (top == -1)
            root = cur;
        else
        {
            par = peek();
            if (cur->data < par->data)
                par->l = cur;
            else
                par->r = cur;
        }
    }

    return root;
}

void preorder(Node *root)
{
    if (root != NULL)
    {
        printf("%d ", root->data);
        preorder(root->l);
        preorder(root->r);
    }
}
int successor(Node* root,int val)
{
    if(root)
    {
        successor(root->l,val);
        if(z==1)
        {
            z=0;
            return root->data;}
        if(root->data==val)
        z=1;
        successor(root->r,val);
    }
}
int predecessor(Node* root,int val)
{
    if(root)
    {
        predecessor(root->r,val);
        if(q==1)
        {q=0;
        return root->data;}
        if(root->data==val)
        q=1;
        predecessor(root->l,val);
    }
}


int main()
{
    // 25 26 28 23 22 24 27
    // 5 6 8 3 2 4 7
    Node *root = NULL;
    int n,k;
    printf("Enter number of elements: ");
    scanf("%d", &n);

    int temp;
    printf("Enter elements: ");
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &temp);
        root = insertNode(root, temp);
    }
    Node* tempe=root;
    printf("\nPreorder: ");
    preorder(tempe);
    printf("\n");
    printf("Enter a key");
    scanf("%d",&k);
    tempe=root;
    int tem=successor(tempe,k);
    printf("Successor of %d is:%d\n",k,tem);
    tempe=root;
    tem=predecessor(tempe,k);
    printf("Predecessor of %d is:%d\n",k,tem);
    return 0;
} 
