#include<stdio.h>
int opcount=0;
unsigned int conseccheck(unsigned int m, unsigned int n,unsigned int t)
{
	opcount++;
	if(m%t==0&&n%t==0)
	return t;
	else
	{
		return conseccheck(m,n,t-1);
	}
}
int main() {
	unsigned int m,n;
	printf("Enter the two numbers whose GCD has to be calculated");
	scanf("%d", &m);
	scanf("%d", &n);
	printf("\nGCD of two numbers using consecutive integer checking method is ");
	unsigned int t=conseccheck(m,n,m<n?m:n); 
	printf("%d",t);
	printf("\nNo. of operations:%d\n",opcount);
	return 0;
}