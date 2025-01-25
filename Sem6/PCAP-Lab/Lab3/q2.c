// Question 2 Write a MPI program to read an integer value M and NXM elements into an 1D array in the
// root process, where N is the number of processes. Root process sends M elements to each
// process. Each process finds average of M elements it received and sends these average values
// to root. Root collects all the values and finds the total average. Use collective communication
// routines.
#include "mpi.h"
#include <stdio.h>
int main(int argc, char *argv[])
{
    int rank,size,N,M,A[100],C[10],i,chunk;
    float avg=0,B[10];
    MPI_Init(&argc,&argv);
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    MPI_Comm_size(MPI_COMM_WORLD,&size);
    if(rank==0)
    {
        N=size;
        printf("Enter the value of M: ");
        scanf("%d",&M);
        printf("Enter %d values:\n",N*M);
        for(i=0; i<N*M; i++)
            scanf("%d", &A[i]);
        chunk=M;
    }
    MPI_Bcast(&chunk,1,MPI_INT,0,MPI_COMM_WORLD);
    MPI_Scatter(A,chunk, MPI_INT,C,chunk,MPI_INT,0,MPI_COMM_WORLD);
    for(i=0;i<chunk;i++) 
        avg+=C[i];
    MPI_Gather(&avg,1,MPI_FLOAT,B,1,MPI_FLOAT,0,MPI_COMM_WORLD);
    fprintf(stdout,"Average of elements in rank:%d is = %.2f\n",rank,avg/chunk);
    if(rank==0)
    {
        // fprintf(stdout,"\nThe Result gathered in the root \n");
        avg=0;
        for(i=0; i<N; i++)
        {
            // fprintf(stdout,"%f \t",B[i]);
            avg+=B[i];
        }
        fprintf(stdout,"\nTotal Average: %.2f\n",avg/(N*M));
    }
    fflush(stdout);
    MPI_Finalize();
    return 0;
}
// Enter the value of M: 2
// Enter 10 values:
// 1 2 3 4 5 6 7 8 9 10
// Average of elements in rank:0 is = 1.50
// Average of elements in rank:1 is = 3.50
// Average of elements in rank:2 is = 5.50
// Average of elements in rank:3 is = 7.50
// Average of elements in rank:4 is = 9.50
// Total Average: 5.50
