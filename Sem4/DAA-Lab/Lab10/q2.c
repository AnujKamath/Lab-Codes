#include <stdio.h>
#include <stdlib.h>
#define infinity 99999
int opcount;
typedef struct
{
    int V;
    int** adjM;
}Graph;

Graph* createGraph(int V) {
    Graph* g = (Graph*)malloc(sizeof(Graph));
    g->V = V;
    g->adjM = (int**)calloc(V,sizeof(int*));
    for (int i = 0; i < V; ++i)
    {
        g->adjM[i]=(int*)calloc(V,sizeof(int));
        for( int j=0;j<V;j++)
        {
            if(i==j)
                g->adjM[i][j]=0;
            else
                g->adjM[i][j] = infinity;
        }
    }
    return g;
}
void addEdge(Graph* g, int s, int d,int v) {
    g->adjM[s][d]=v;
}

void printMatrix(Graph *g)
{
    printf("\nAdjacency Matrix: \n");
    for (int i = 0; i < g->V; i++)
    {
      for(int j=0;j<g->V;j++)
      {
        printf("%d ",g->adjM[i][j]);
      }
      printf("\n");
    }
    printf("\n");
}
void FloydAlgo(Graph* g)
{
    for(int a=0;a<g->V;a++)
    {
        for(int i=0;i<g->V;i++)
        {
            for(int j=0;j<g->V;j++)
            {
                if(g->adjM[i][a]==infinity) break;
                opcount++;
                if(g->adjM[a][j]+g->adjM[i][a]<g->adjM[i][j])
                {
                    g->adjM[i][j]=g->adjM[a][j]+g->adjM[i][a];
                }
            }
        }
    }
}

int main() {
    opcount=0;
    int V = 4;
    Graph* graph = createGraph(V);
    addEdge(graph, 1,0,2);
    addEdge(graph, 0,2, 3);
    addEdge(graph, 2,1, 7);
    addEdge(graph, 2, 3,1);
    addEdge(graph, 3,0,6);
    printMatrix(graph);
    FloydAlgo(graph);
    printMatrix(graph);
    printf("The opcount is:%d\n",opcount);
    return 0;
}
