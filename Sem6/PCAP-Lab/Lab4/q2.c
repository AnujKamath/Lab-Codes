// Write a MPI program to read a 3 X 3 matrix. Enter an element to be searched in the root
// process. Find the number of occurrences of this element in the matrix using three processes.
#include <stdio.h>
#include "mpi.h"
int main(int arge, char* argv[])
{ 
    int rank,size;
    int A[3][3], b[3];
    int one=0,zero=0, sum=0,n,f=0;
    MPI_Init(&arge, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    if(rank==0)
    {
        printf("Enter 9 elements\n");;
        for(int i=0;i<3;i++)
            for(int j=0;j<3;j++)
                scanf("%d",&A[i][j]);
        printf("Enter the number to be searched:");
        scanf("%d",&n);
    }
    MPI_Bcast( &n , 1 , MPI_INT , 0 , MPI_COMM_WORLD);
    MPI_Scatter(&A,3, MPI_INT, &b, 3, MPI_INT,0, MPI_COMM_WORLD);
    for(int i=0;i<3;i++)
    {
        if(b[i]==n)
            one=1;
        MPI_Scan(&one,&sum, 1, MPI_INT, MPI_SUM, MPI_COMM_WORLD);

    }
    MPI_Reduce(&sum,&f, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);
    if(rank==0)
    {
        printf("Number of occurences of %d = %d\n",n, f);
    }
    MPI_Finalize();
    return 0;
}