#include <stdio.h>
#include <stdlib.h>
typedef struct Node {
    int data;
    struct Node* next;
}Node;
typedef struct Graph {
    int V;
    struct Node** array;
}Graph;
 Node* newNode(int data) {
     Node* node = ( Node*)malloc(sizeof( Node));
    node->data = data;
    node->next = NULL;
    return node;
}
Graph* createGraph(int V) {
    Graph* graph = ( Graph*)malloc(sizeof(Graph));
    graph->V = V;
    graph->array = ( Node**)malloc(V * sizeof(Node*));
    for (int i = 0; i < V; ++i)
        graph->array[i] = NULL;
    return graph;
}
void addEdge(Graph* graph, int src, int dest) {
     Node* node = newNode(dest);
    node->next = graph->array[src];
    graph->array[src] = node;
    node = newNode(src);
    node->next = graph->array[dest];
    graph->array[dest] = node;
}
typedef struct Stack {
    int top;
    unsigned capacity;
    int* array;
}Stack;
Stack* createStack(unsigned capacity) {
    Stack* stack = (Stack*)malloc(sizeof(Stack));
    stack->capacity = capacity;
    stack->top = -1;
    stack->array = (int*)malloc(stack->capacity * sizeof(int));
    return stack;
}
int isEmpty(Stack* stack) {
    return stack->top == -1;
}
void push(Stack* stack, int item) {
    stack->array[++stack->top] = item;
    printf("Pushed %d\n", item);
}
int pop(Stack* stack) {
    int item = stack->array[stack->top--];
    printf("Popped %d\n", item);
    return item;
}
void DFSUtil(Graph* graph, int v, int visited[], Stack* stack) {
    visited[v] = 1;
    push(stack, v);
    Node* node = graph->array[v];
    while (node != NULL) {
        if (!visited[node->data])
            DFSUtil(graph, node->data, visited, stack);
        node = node->next;
    }
    pop(stack);
}
void DFS(Graph* graph) {
    Stack* stack = createStack(graph->V);
    int* visited = (int*)malloc(graph->V * sizeof(int));
    for (int i = 0; i < graph->V; i++)
        visited[i] = 0;
    for (int i = 0; i < graph->V; i++)
        if (visited[i] == 0)
            DFSUtil(graph, i, visited, stack);
    free(stack->array);
    free(stack);
    free(visited);
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
    printf("\nPush and pop order in DFS traversal:\n");
    DFS(graph);
    return 0;
}
