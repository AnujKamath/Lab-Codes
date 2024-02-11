#include <stdio.h>
#include <stdlib.h>
typedef struct n
{
    int val;
    struct n* next;
}Node;

typedef struct
{
    int V;
    Node** adjList;
    int* inorder;
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
    g->inorder=(int*)calloc(V,sizeof(int));
    for(int i = 0; i < V; ++i)
        g->adjList[i] = NULL;
    return g;
}
void addEdge(Graph* g, int s, int d) {
	Node *temp = newNode(d);
	temp -> next = g->adjList[s];
	g->adjList[s] = temp;
    g->inorder[d]++;
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
    printf("\nInOrder List: \n");
    for (int v = 0; v < graph->V; v++)
    {
        printf("\n Inorder for Vertex %d: %d\n", v,graph->inorder[v]);
    }
}
void remove_ties(Graph* g,int v)
{
    Node* temp=g->adjList[v];
    while(temp)
    {
        g->inorder[temp->val]--;
        temp=temp->next;
    }
    free(temp);
}
void toposort(Graph* g)
{
    printf("Topological Sorting Using Source Removal Method: ");
    int* vis=(int*)calloc(g->V,sizeof(int));
    while(1)
    {
        int c=0;
        for(int i=0;i<g->V;i++)
        {
            if(g->inorder[i]==0&&!vis[i])
            {
                c++;
                vis[i]=1;
                printf("%d ",i);
                remove_ties(g,i);
            }
        }
        if(c==0)
        break;
    }
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
