// Write a MPI program to read a 3 X 3 matrix. Enter an element to be searched in the root
// process. Find the number of occurrences of this element in the matrix using three processes.
#include <stdio.h>
#include "mpi.h"
int main(int arge, char* argv[])
{ 
    int rank,size,n=4;
    int A[n][n], b[n],c[n];
    for(int i=0;i<n;i++) c[i]=0;
    MPI_Init(&arge, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    if(rank==0)
    {
        printf("Enter %d elements\n",n);
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++)
                scanf("%d",&A[i][j]);
    }
    MPI_Scatter(&A,n, MPI_INT, &b, n, MPI_INT,0, MPI_COMM_WORLD);

    MPI_Scan(&b,&c,n,MPI_INT,MPI_SUM, MPI_COMM_WORLD);
    
    MPI_Gather(&c,n,MPI_INT,&A,n,MPI_INT,0,MPI_COMM_WORLD);
    if(rank==0)
    {
        printf("Resultant array\n");
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
                printf("%d ",A[i][j]);
            printf("\n");
        }
    }
    MPI_Finalize();
    return 0;
}