
#include <stdio.h>
#include <stdlib.h>
int opcount=0;
typedef struct t{
    int val;
    struct t* l;
    struct t* r;
}Tree;

Tree* populate(int* ar) {
    static int i=0;
    if(ar[i]==-9999||ar[i]==-1)
    {
        return NULL;
    }
    Tree* x=(Tree*)malloc(sizeof(Tree));
    x->val=ar[i];
    i++;
    x->l=populate(ar);
    i++;
    x->r=populate(ar);
	return x;
}
int no_of_node(Tree* t)
{
    opcount++;
    if(t) return 1+no_of_node(t->l)+ no_of_node(t->r);
    else return 0;
}

int main() {
    int arr[]={1,2,-1,3,-1,-1,4,5,-1,-1,6,-1,-1,-9999};
    int i=0;
    Tree* tr=populate(arr);
    printf("The numberof nodes in the tree is: %d",no_of_node(tr));
    printf("\nThe opcount is %d",opcount);
    return 0;
}