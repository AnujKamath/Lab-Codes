#include <stdio.h>
#include <stdlib.h>
typedef struct Node
{
    int vert;
    struct Node* next;
}Node;
typedef struct graph{
    int v;
    int** adjm;
    Node** adjl;
} graph;
Node* createNode(int x)
{
    Node* temp=(Node*)malloc(sizeof(Node));
    temp->next=NULL;
    temp->vert=x;
    return temp;
}
graph* createGraph(int nv)
{
    graph* root=(graph*)malloc(sizeof(graph));
    root->v=nv;
    root->adjl=(Node**)calloc(nv,sizeof(Node*));
    root->adjm=(int**)calloc(nv, sizeof(int*));
    int i=0,j=0;
    for(i=0;i<nv;i++)
    {
        root->adjl[i]=NULL;

        root->adjm[i]=(int*)calloc(nv,sizeof(int));
        for(j=0;j<nv;j++)
        root->adjm[i][j]=0;
    }
    return root;
}
void addEdge(graph* g, int s, int d)
{
    g->adjm[s-1][d-1]=1;
    Node* temp=createNode(d);
    temp->next=g->adjl[s-1];
    g->adjl[s-1]=temp;
}
void printgraph(graph* g)
{
    int i=0,j=0;
    printf("Adjacency Matrix\n");
    for(i=0;i<g->v;i++)
    {
        for(j=0;j<g->v;j++)
        printf("%d ",g->adjm[i][j]);
        printf("\n");
    }
    printf("Adjacency List\n");
    for(i=0;i<g->v;i++)
    {
        Node* temp=g->adjl[i];
        printf("%d:",i+1);
        while(temp)
        {        
            printf("-> %d",temp->vert);
            temp=temp->next;
        }
        printf("\n");
    }
}
int main()
{
  graph* root = createGraph(4);
  addEdge(root, 1, 2);
  addEdge(root, 1, 3);
  addEdge(root, 1, 4);
  addEdge(root, 2, 3);

  printgraph(root);

  return 0;
}
