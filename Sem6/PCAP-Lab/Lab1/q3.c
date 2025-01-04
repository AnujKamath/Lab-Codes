
/*Write a program in MPI to simulate simple calculator. Perform each operation using different process in parallel.*/
#include "mpi.h"
#include <stdio.h>
int main(int argc, char* argv[])
{
	int rank,size;
	int a=5,b=3;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	switch(rank)
	{
		case 1:
		printf("%d + %d = %d\n", a,b,a+b);
		break;
		case 2:
		printf("%d - %d = %d\n", a,b,a-b);
		break;
		case 3:
		printf("%d / %d = %.2f\n", a,b,(1.0*a)/b);
		break;
		case 4:
		printf("%d * %d = %d\n", a,b,a*b);
		break;
		default:
		printf("Only basic math operations\n");
	}
	MPI_Finalize();
	return 0;
}
/*
Only basic math operations
5 + 3 = 8
5 - 3 = 2
5 * 3 = 15
5 / 3 = 1.67
*/
