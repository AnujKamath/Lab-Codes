
/*Write a simple MPI program to find out pow (x, rank) for all the processes where 'x' is the 
integer constant and 'rank' is the rank of the process.*/
#include "mpi.h"
#include <stdio.h>
#include <math.h>
int main(int argc, char* argv[])
{
	int rank,size,x=3;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	
	printf("My rank is %d, value of pow is= %f\n", rank,pow(x,rank));
	MPI_Finalize();
	return 0;
}
/*
My rank is 0, value of pow is= 1.000000
My rank is 1, value of pow is= 3.000000
My rank is 2, value of pow is= 9.000000
*/
