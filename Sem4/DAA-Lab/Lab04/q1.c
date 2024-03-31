#include <stdio.h>
#include <stdlib.h>
int c=9999999;
int* sub;
int n;
int opcount=0;
void copy(int vis[])
{
	for(int i=0;i<n;i++)
	{
		sub[i]=vis[i];
	}
}
void checker(int a[][4],int vis[],int sum,int r)
{	
	if(r==n)
	{
		if(c>sum)
		{
			opcount++;
			c=sum;
			copy(vis);
		}
		return;
	}
	for(int i=0;i<n;i++)
	{
		if(vis[i]==-1)
		{
			opcount++;
			vis[i]=r;
			checker(a,vis,sum+a[r][i],r+1);
			vis[i]=-1;
		}
	}
}
int main()
{
	sub=(int*)malloc(sizeof(int));
	n=4;
	int a[4][4]={
        {10, 3, 8, 9},
        {7, 5, 4, 8},
        {6, 9, 2, 9},
        {8, 7, 10, 5}
    };
    int vis[]={-1,-1,-1,-1};
    checker(a,vis,0,0);
    printf("\nIndices: ");
    for(int i=0;i<n;i++)
    {
    	printf("%d ",sub[i]);
    }
    printf("\nTotal Cost: %d\n",c);
    printf("\nOPCOUNT: %d\n",opcount);
    return 0;

}
