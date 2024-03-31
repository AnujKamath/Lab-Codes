#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int opcount = 0;
typedef struct Node
{
    int a;
    struct Node *next;
} Node;

void insertNode(Node **head, int sum, Node *temp)
{
    Node *temper = head[sum];
    if (!temper)
        head[sum] = temp;
    else
    {
        while (temper->next)
        {
            temper = temper->next;
        }
        temper->next = temp;
    }
}
Node **makeOpenTable(int a[], int k, int m)
{
    Node **head = (Node **)calloc(k, sizeof(Node *));
    for (int i = 0; i < k; i++)
    {
        head[i] = NULL;
    }
    Node *temp;
    for (int i = 0; i < m; i++)
    {
        temp = (Node *)malloc(sizeof(Node));
        temp->next = NULL;
        temp->a = a[i];
        insertNode(head, a[i] % k, temp);
    }
    return head;
}
int search(Node **head, int key, int k)
{
    opcount = 0;
    Node *temp = head[key % k];
    while (temp)
    {
        opcount++;
        if (temp->a == key)
            return 1;
        temp = temp->next;
    }
    return 0;
}
int main()
{
    int k, m, key;
    printf("Enter the value of m and n");
    scanf("%d %d", &m, &k);
    int s[m];
    for (int i = 0; i < m; i++)
    {
        s[i] = i + 1;
    }
    Node **head = makeOpenTable(s, k, m);
    printf("Enter the key to be searched");
    scanf("%d", &key);
    if (search(head, key, k))
        printf("Key found\n");
    else
        printf("Key not found\n");
    printf("No of key comparisons: %d\n", opcount);
    return 0;
}