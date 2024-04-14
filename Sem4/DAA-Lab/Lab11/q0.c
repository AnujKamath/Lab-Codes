#include<stdio.h>
#include<conio.h>
int a[50][50],t[50][50],root[50],parent[50],n,i,j,value,e=0,k=0;
int ivalue,jvalue,cost=0,mincost=0,TV[50],count=0,present=0;

void read_cost()
{
    printf("\n Enter the number of vertices:");
    scanf("%d",&n);
    printf("\n Enter cost adjacency matrix\n");
    for(i=1;i<=n;i++)
        for(j=1;j<=n;j++)
            if(i<j)
            {
                printf("(%d,%d):",i,j);
                scanf("%d",&value);
                a[i][j]=value;
                if(value!=0)
                    e++;
            }
            else if(i>j)
                a[i][j]=a[j][i];
            else
                a[i][j]=0;
}
int check_reach(int v)
{
    int p;
    for(p=1;p<=count;p++)
    if(TV[p]==v) return 1;
    return 0;
}
void prims()
{
    while(e && k<n-1)
    {
        for(i=1;i<=n;i++)
            for(j=1;j<=n;j++)
            {
                if(a[i][j]!=0)
                {
                    int x,y;
                    x=check_reach(i);
                    y=check_reach(j);
                    if((x==1) && (y==0))
                    {
                        present=1;
                        if((a[i][j] < cost) || (cost==0))
                        {
                            cost=a[i][j];
                            ivalue=i;
                            jvalue=j;
                        }
                    }
                }
            }
        if(present==0) break;
        a[ivalue][jvalue]=0;
        a[jvalue][ivalue]=0;
        e--;
        TV[++count]=jvalue;
        t[ivalue][jvalue]=cost;
        k++;
        present=cost=0;
    }
}
void display()
{
    if(k==n-1)
    {
        printf("\n Minimum cost spanning tree is\n");
        for(i=1;i<=n;i++)
            for(j=1;j<=n;j++)
            {
                if(t[i][j]!=0)
                    printf("\n(%d,%d):%d",i,j,t[i][j]);
                mincost=mincost+t[i][j];
            }
        printf("\n Cost of this spanning tree:%d",mincost);
    }
    else
    printf("\n Graph is not connected");
}

int main()
{
    printf("\n\t\t\t PRIMS ALGORITHM\n");
    TV[++count]=1;
    read_cost();
    prims();
    display();
    // getch();
}
//                          PRIMS ALGORITHM

//  Enter the number of vertices:6

//  Enter cost adjacency matrix
// (1,2):3
// (1,3):0
// (1,4):0
// (1,5):6
// (1,6):5
// (2,3):1
// (2,4):0
// (2,5):0
// (2,6):4
// (3,4):6
// (3,5):0
// (3,6):4
// (4,5):8
// (4,6):5
// (5,6):2

//  Minimum cost spanning tree is

// (1,2):3
// (2,3):1
// (2,6):4
// (6,4):5
// (6,5):2
//  Cost of this spanning tree:15
