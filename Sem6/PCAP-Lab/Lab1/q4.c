
/*Write a program in MPI to toggle the character of a given string indexed by the rank of the process. Hint: Suppose the string is HELLO and there are 5 processes, then process 0 toggle 'H' to 'h', process 1 toggle 'E' to 'e' and so on.*/
#include "mpi.h"
#include <stdio.h>
int main(int argc, char* argv[])
{
	int rank,size;
	char str[]="Anuj";
	//printf("Initial String = %s\n", str);
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	if(str[rank]>=97)
		str[rank]-=32;
	else 
		str[rank]+=32;
	MPI_Finalize();
	printf("Rank:%d || Resultant String is = %s\n", rank, str);
	return 0;
}
/*
Rank:0 || Resultant String is = anuj
Rank:1 || Resultant String is = ANuj
Rank:2 || Resultant String is = AnUj
Rank:3 || Resultant String is = AnuJ
*/
