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
}Graph;
typedef struct
{
    int *data;
    int front;
    int rear;
    int size;
} Queue;

Queue *createQueue(int size)
{
    Queue *temp = (Queue *)calloc(1, sizeof(Queue));
    temp->size = size;
    temp->data = (int *)calloc(size, sizeof(int));
    temp->front = -1;
    temp->rear = -1;
    return temp;
}
int isQEmpty(Queue *q)
{
    return (q->rear == -1 && q->front == -1);
}

void insertQ(Queue *q, int x)
{
    if (isQEmpty(q))
    {
        q->front = 0;
        q->rear = 0;
    }
    else
    {
        q->rear = (q->rear + 1) % (q->size);
    }
    q->data[q->rear] = x;
}

int deleteQ(Queue *q){
    if(isQEmpty(q)){
        printf("Queue is empty!\n");
        return -69;
    }
    int x = q->data[q->front];
    if(q->front == q->rear){
        q->rear = -1;
        q->front = -1;
    }
    else
        q->front = (q->front+1)%(q->size);
    
    return x;
}
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
void printArr(int arr[],int n)
{
	for(int i=0;i<n;i++)
		printf("\nInserted %d",arr[i]);
}
void BFS(Graph* g,int start) {
	int vis[g->V];
	for(int i=0;i<g->V;i++)
		vis[i]=0;
	Queue* q=createQueue(g->V);
	insertQ(q,start);
	int pushOrder[g->V];
	int i=0;
	pushOrder[i++]=start;
	while(!isQEmpty(q))
	{
		int t=deleteQ(q);
		Node* d=g->adjList[t];
		while(d!=NULL)
		{
			if(vis[d->val]==0)
			{
				pushOrder[i++]=d->val;
				vis[d->val]=1;
				insertQ(q,d->val);
			}
			d=d->next;
		}
	}
	printArr(pushOrder,i); 
}
int main() {
    int V = 7;
    Graph* graph = createGraph(V);
    addEdge(graph, 0, 1);
    addEdge(graph, 0, 2);
    addEdge(graph, 1, 3);
    addEdge(graph, 1, 4);
    addEdge(graph, 2, 5);
    addEdge(graph, 3, 6);
    addEdge(graph, 4, 5);
    addEdge(graph, 5, 6);
    printf("\nPush order in BFS traversal:\n");
    BFS(graph,0);
    return 0;
}
