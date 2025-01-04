/*Write a program in MPI where even ranked process prints factorial of the rank and odd ranked process prints ranks Fibonacci number.*/
#include "mpi.h"
#include <stdio.h>
int factorial(int n)
{
	int ans=1;
	for(int i=2;i<=n; i++) ans*=i;
	return ans;
}
int fib(int n)
{
	if(n<2) return n;
	return fib(n-1) + fib(n-2);
}
int main(int argc, char* argv[])
{
	int rank,size;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	if(rank%2==0)
		printf("Rank: %d || Factorial is = %d\n", rank, factorial(rank));
	else 
		printf("Rank: %d || Fibonacci Number is = %d\n", rank, fib(rank));
	MPI_Finalize();
	return 0;
}
/*
Rank: 0 || Factorial is = 1
Rank: 1 || Fibonacci Number is = 1
Rank: 2 || Factorial is = 2
Rank: 3 || Fibonacci Number is = 2
Rank: 4 || Factorial is = 24
*/
