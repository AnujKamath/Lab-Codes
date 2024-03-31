#include <stdio.h>
int opcount=0;
void smatch(char s[],char sub[])
{
	int f=-1,m=0,n=0;
	for(;s[m]!='\0';m++,opcount++);
	for(;sub[n]!='\0';n++,opcount++);
	for(int i=0;i<m-n+1;i++)
	{
		int j=0;
		opcount++;
		if(s[i]==sub[j])
		{
			while(j<n&&s[i+j]==sub[j])
			{
				opcount++;
				j++;
			}
			if(j==n)
				f=i;
		}
	}
	if(f==-1)
		printf("No match");
	else
		printf("Substring found at index %d",f);
}
int main()
{
	int n,i;
	char s[100],sub[100];
	printf("Enter the main string: ");
	scanf("%s",s);
	printf("Enter the substring: ");
	scanf("%s",sub);
	smatch(s,sub);
	printf("\nOpcount= %d\n",opcount);
	return 0;
}
