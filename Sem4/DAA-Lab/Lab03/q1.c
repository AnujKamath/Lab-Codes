#include <stdio.h>
int comp=0,swap=0;
void bubblesort(int a[],int n)
{
	int i,j;
	for(i=0;i<n-1;i++)
	{
		for(j=0;j<n-1-i;j++)
		{
			comp+=1;
			if(a[j]>a[j+1])
			{
				swap+=3;
				int t=a[j];
				a[j]=a[j+1];
				a[j+1]=t;
			}
		}
	}
}
int main()
{
	int n,i;
	printf("Enter the number of elements");
	scanf("%d",&n);
	int a[n];
	printf("Enter %d numbers",n);
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
	printf("Elements before sorting: ");
	for(i=0;i<n;i++)
		printf("%d ",a[i]);
	printf("\nElements after sorting: ");
	bubblesort(a,n);
	for(i=0;i<n;i++)
		printf("%d ",a[i]);
	printf("\nOperation Count= %d",comp+swap);

	return 0;
}
