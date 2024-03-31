#include <stdio.h>
#include <stdlib.h>
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
        g->adjM[i][j] = 0;
    }
    return g;
}
void addEdge(Graph* g, int s, int d) {
    g->adjM[s][d]=1;
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
void warshallAlgo(Graph* g)
{
    for(int a=0;a<g->V;a++)
    {
        for(int i=0;i<g->V;i++)
        {
            for(int j=0;j<g->V;j++)
            {
                if(g->adjM[i][a]==0)
                break;
                opcount++;
                if(g->adjM[a][j]==1&&g->adjM[i][a]==1)
                {
                    g->adjM[i][j]=1;
                }
            }
        }
    }
}


int main() {
    opcount=0;
    int V = 5;
    Graph* graph = createGraph(V);
    addEdge(graph, 0, 1);
    addEdge(graph, 1, 3);
    addEdge(graph, 1, 2);
    addEdge(graph, 2, 4);
    addEdge(graph, 4, 0);
    // addEdge(graph, 0, 1);
    // addEdge(graph, 2, 3);
    // addEdge(graph, 1, 2);

    printMatrix(graph);
    warshallAlgo(graph);
    printMatrix(graph);
    printf("The opcount is:%d\n",opcount);
    return 0;
}
