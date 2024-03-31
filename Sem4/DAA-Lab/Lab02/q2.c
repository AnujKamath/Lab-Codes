#include<stdio.h>
int opcount=0;
int nextPrime(int x,int i)
{
	i=i%2?i+2:i+1;
	for(;i<x;i++)
	{
		int f=0;
		if(x%i==0)
		{
			if(i%2==0)
				f=1;
			for(int j=3;j<i/2;j+=2)
			{
				opcount+=1;
				if(i%j==0)
				{f=1;break;}

			}
			if(f==0)
				return i;
		}
	}
	return i;
}
int findgcd(int m,int n)
{
	int c=m,d=n;
	int f=2;
	int ans=1;
	while(f<=m&&f<=n)
	{
		while(m%f==0&&n%f==0)
		{
			opcount++;
			ans*=f;
			m/=f;
			n/=f;
			printf("%d ",f);
		}
		int x=nextPrime(c,f);
		int y=nextPrime(d,f);
		// printf("%d %d\n",x,y);
		while(x!=y)
		{
			opcount++;
			if(x>=c||y>=d)
				return ans;
			if(x>y)
				y=nextPrime(d,y);
			else
				x=nextPrime(c,x);
		}
		f=x;
		// printf("%d\n",f);
	}
	return ans;

}
int main() {
	unsigned int m,n;
	printf("Enter the two numbers whose GCD has to be calculated");
	scanf("%d", &m);
	scanf("%d", &n);
	printf("\nGCD of two numbers using middle school method is ");
	unsigned int t=findgcd(m,n); 
	printf("%d",t);
	printf("\nNo. of operations:%d\n",opcount);
	return 0;
}
