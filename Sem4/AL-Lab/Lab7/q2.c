#include <stdio.h>
#include <stdlib.h>

#define MAX_NODES 100

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
Node* successor(Node* root)
{
    // if(root->r==NULL)
    // return NULL;
    Node* succ=root->r;
    while(succ->l)
    {
        succ=succ->l;
    }
    return succ;
}
Node* predecessor(Node* root)
{
    // if(root->l==NULL)
    // return NULL;
    Node* pred=root->l;
    while(pred->r)
    {
        pred=pred->r;
    }
    return pred;
}
Node* search(Node* root,int key)
{
    // if(!root)
    // return NULL;
    printf("%d\n",root->data);
    if(root->data==key)
    return root;
    if(key<root->data)
    return search(root->l,key);
    else return search(root->r,key);
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

    printf("\nPreorder: ");
    preorder(root);
    printf("\n");
    printf("Enter a key");
    scanf("%d",&k);
    Node* t=search(root,k);
    printf("%d",t->data);
    Node *tem=successor(t);
    // printf("Successor of %d is:%d\n",k,tem->data);
    tem=predecessor(t);
    printf("Predecessor of %d is:%d\n",k,tem->data);
    return 0;
} 