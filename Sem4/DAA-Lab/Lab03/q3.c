#include <stdio.h>
int opcount=0;
int split(int a[],int n, int sum)
{
	if(n==0)
		return 0;
	int b[n];
	int m=0;

}
void partition(int a[],int n)
{
	int sum=0;
	for(int i=0;i<n;i++,sum+=a[i]);
	if(sum%2!=0)
		printf("Partition Not Possible");
	else
		return split(a,n,sum/2);
}
int main()
{
	printf("Enter the size of array");
	scanf("%d",&n);
	int a[n];
	printf("Enter %d numbers",n);
	for(int i=0;i<n;i++)
		scanf("%d", &a[i]);
	partiton(a,n);
	return 0;
}
