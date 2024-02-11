
#include <stdio.h>
#include <stdlib.h>
#include "../Headers/stack.h"
typedef struct n
{
    int val;
    struct n* next;
}Node;

typedef struct
{
    int V;
    Node** adjList;
}Graph;
Node* newNode(int data) {
    Node* node = ( Node*)malloc(sizeof(Node));
    node->val = data;
    node->next = NULL;
    return node;
}
Graph* createGraph(int V) {
    Graph* g = (Graph*)malloc(sizeof(Graph));
    g->V = V;
    g->adjList = (Node**)calloc(V,sizeof(Node*));
    for (int i = 0; i < V; ++i)
        g->adjList[i] = NULL;
    return g;
}
void addEdge(Graph* g, int s, int d) {
	Node *temp = newNode(d);
	temp -> next = g->adjList[s];
	g->adjList[s] = temp;
}

void printList(Graph *graph)
{
    printf("\nAdjacency Lists: \n");
    for (int v = 0; v < graph->V; v++)
    {
        Node *temp = graph->adjList[v];
        printf("\n Vertex %d: ", v);
        while (temp != NULL)
        {
            printf("%d   ", temp->val);
            temp = temp->next;
        }
    }
    printf("\n");
}
void dfs(int v,Graph* g, Stack* s, int* vis)
{
    vis[v]=1;
    Node* temp=g->adjList[v];
    while(temp)
    {
        if(!vis[temp->val])
        {
            dfs(temp->val,g,s,vis);
        }
        temp=temp->next;
    }
    push(s,v);
}
void toposort(Graph* g)
{
    int* vis=(int*)calloc(g->V,sizeof(int));
    Stack* s=createStack(g->V);
    for(int i=0;i<g->V;i++)
    {
        if(!vis[i])
        {
            dfs(i,g,s,vis);
        }
    }
    printf("Topological Sorting Using DFS: ");
    while(!isEmpty(s))
    {
        printf("%d ", pop(s));
    }
    printf("\n");
}

int main() {
    int V = 6;
    Graph* graph = createGraph(V);
    addEdge(graph, 2, 3);
    addEdge(graph, 3, 1);
    addEdge(graph, 5, 0);
    addEdge(graph, 4, 0);
    addEdge(graph, 5, 2);
    addEdge(graph, 4, 1);
    printList(graph);
    toposort(graph);
    return 0;
}
