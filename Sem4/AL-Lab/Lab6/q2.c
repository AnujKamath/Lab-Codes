#include <stdio.h>
#include <stdlib.h>
int opcount=0;
void swap(int *a, int *b)
{
    opcount++;
    int t=*a;
    *a=*b;
    *b=t;
}
void quicksort(int* ar, int f,int l)
{
    if(f<l)
    {
        // int pivot=f;
        int i=f,j=l;
        while(i<j)
        {
            for(;i<=l&&ar[f]>=ar[i];i++,opcount++);
            for(;j>f&&ar[f]<=ar[j];j--,opcount++);
            if(i<j)
            {
                swap(&ar[i],&ar[j]);
            }

        }
        swap(&ar[f],&ar[j]);
        quicksort(ar,f,j-1);
        quicksort(ar,j+1,l);
    }
}
int main()
{
    int ar[]={0,1,2,3,4,5,6,7,8,9};
    quicksort(ar,0,9);
    printf("After quicksort: ");
    for(int i=0;i<10;i++)
        printf("%d ",ar[i]);
    printf("\nThe Opcount is %d\n", opcount);
    return 0;
}