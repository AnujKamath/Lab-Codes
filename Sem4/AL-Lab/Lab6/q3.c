#include <stdio.h>
#include <stdlib.h>
int opcount=0;
void merge(int* a, int l,int m,int r)
{
    int n1=m-l+1,n2=r-m;
    int ar1[n1],ar2[n2];
    int i=l,x=0,y=0;
    while(x<n1)
    {ar1[x]=a[l+x];x++;}
    while(y<n2)
    {ar2[y]=a[m+1+y];y++;}
    x=y=0;
    while(x<n1 && y<n2)
    {
        if(ar2[y]<=ar1[x])
        a[i++]=ar2[y++];
        else
        a[i++]=ar1[x++];
        opcount++;
    }
    while(y<n2)
        a[i++]=ar2[y++];
    while(x<n1)
        a[i++]=ar1[x++];
}
void mergesort(int* a,int l,int r)
{
    if(l>=r)
    return;
    opcount++;
    int m=l+(r-l)/2;
    mergesort(a,l,m);
    mergesort(a,m+1,r);
    printf("%d, %d, %d,\n",l,m,r);
    merge(a,l,m,r);
}
int main()
{
    int ar[]={3,2,1,6,7,4,5};
    int s=7;
    mergesort(ar,0,s-1);
    printf("After mergesort: ");
    for(int i=0;i<s;i++)
        printf("%d ",ar[i]);
    printf("\nThe Opcount is %d\n", opcount);
    return 0;
}
