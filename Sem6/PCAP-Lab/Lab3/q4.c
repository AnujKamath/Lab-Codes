// Write a MPI Program to read two strings S1 and S2 of same length in the root process. Using
// N processes including the root (string length is evenly divisible by N), produce the resultant
// string as shown below. Display the resultant string in the root process. Use Collective
// communication routines.
// Example:
// String S1: string
// String S2: length
// Resultant String : slternigntgh
#include "mpi.h"
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    int rank,size,N,l,i,chunk,x=0;
    char A1[100],A2[100],B1[10],B2[10],res[100],C[20];
    MPI_Init(&argc,&argv);
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    MPI_Comm_size(MPI_COMM_WORLD,&size);
    if(rank==0)
    {
        N=size;
        printf("Enter first string: ");
        scanf("%s",A1);
        printf("Enter second string: ");
        scanf("%s",A2);
        l=strlen(A1);
        chunk=l/N;
    }
    MPI_Bcast(&chunk,1,MPI_INT,0,MPI_COMM_WORLD);
    MPI_Bcast(&l,1,MPI_INT,0,MPI_COMM_WORLD);

    MPI_Scatter(A1,chunk, MPI_CHAR,B1,chunk,MPI_CHAR,0,MPI_COMM_WORLD);
    MPI_Scatter(A2,chunk, MPI_CHAR,B2,chunk,MPI_CHAR,0,MPI_COMM_WORLD);

    for(i=0;i<chunk;i++) 
    {
        C[x++]=B1[i];
        C[x++]=B2[i];
    }
    MPI_Gather(C,chunk*2,MPI_CHAR,res,chunk*2,MPI_CHAR,0,MPI_COMM_WORLD);
    if(rank==0)
    {
        res[l*2]='\0';
        fprintf(stdout,"\nResultant String: %s\n",res);
    }
    fflush(stdout);
    MPI_Finalize();
    return 0;
}
// student@dbl-34:~/Documents/220962446_PCAP/Lab3$ mpirun -n 2 ./out1
// Enter first string: string
// Enter second string: length

// Resultant String: slternigntgh


