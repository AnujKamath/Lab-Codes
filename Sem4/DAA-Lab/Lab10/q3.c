#include<stdio.h>
#include<stdlib.h>
int n,W;
int** v;
int max(int a,int b)
{
    return a>b?a:b;
}
int bottomUp(int val[],int w[])
{
    v=(int**)calloc(n+1,sizeof(int*));
    for(int i=0;i<=W;i++)
    {
        v[i]=(int*)calloc(W+1,sizeof(int));
        v[0][i]=0;
    }
    for(int i=0;i<=n;i++)
    v[i][0]=0;
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=W;j++)
        {
            if((j-w[i-1])>=0)
            {
                v[i][j]=max(v[i-1][j],val[i-1]+v[i-1][j-w[i-1]]);
            }
            else{
                v[i][j]=v[i-1][j];
            }
        }
    }
    for(int i=0;i<=n;i++)
    {
        for(int j=0;j<=W;j++)
        printf("%d ",v[i][j]);
        printf("\n");
    }
    return v[n][W];
}
void subset(int* w)
{
    int i=n,j=W;
    printf("The Subset is: ");
    while(i!=0)
    {
        if(v[i][j]!=v[i-1][j])
        {
            printf("%d,",i);
            i--;
            j-=w[i];
        }
        else{
            i--;
        }
    }
    printf("\n");
}
int main()
{
    n=4;
    W=5;
    int val[4]={12,10,20,15};
    int w[4]={2,1,3,2};
    printf("Maximum value of subset:%d\n",bottomUp(val,w));
    subset(w);
    return 0;
}
