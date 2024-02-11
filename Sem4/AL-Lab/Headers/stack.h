typedef struct
{
    int *data;
    int size;
    int top;
} Stack;

Stack *createStack(int size)
{
    Stack *temp = (Stack *)malloc(sizeof(Stack));
    temp->size = size;
    temp->top=-1;
    temp->data = (int *)calloc(size, sizeof(int));
    return temp;
}
int isEmpty(Stack *s)
{
    return (s->top==-1);
}
int isFull(Stack *s)
{
    return (s->top==s->size-1);
}

void push(Stack *s, int x)
{
    if(isFull(s))
    printf("Stack is Full");
    else
    s->data[++(s->top)]=x;
}

int pop(Stack *s){
    if(isEmpty(s)){
        printf("Queue is empty!\n");
        return -69;
    }
    return s->data[(s->top)--];
}
void printStack(Stack* s)
{
    printf("Elements in the stack are:");
    for(int i=0;i<=s->top;i++)
    {
        printf("%d",s->data[i]);
    }
}
