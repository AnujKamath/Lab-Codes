// Question 1 Write a MPI program to read N values in the root process. Root process sends one value to each
// process. Every process receives it and finds the factorial of that number and returns it to the
// root process. Root process gathers the factorial and finds sum of it. Use N number of
// processes.
#include "mpi.h"
#include <stdio.h>
int factorial(int n)
{
    if(n<2) return 1;
    return n*factorial(n-1);
}
int main(int argc, char *argv[])
{
    int rank,size,N,A[10],B[10],c,i,sum=0;
    MPI_Init(&argc,&argv);
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    MPI_Comm_size(MPI_COMM_WORLD,
    &size);
    if(rank==0)
    {
        N=size;
        fprintf(stdout,"Enter %d values:\n",N);
        fflush(stdout);
        for(i=0; i<N; i++)
            scanf("%d", &A[i]);
    }
    MPI_Scatter(A,1, MPI_INT,&c,1,MPI_INT,0,MPI_COMM_WORLD);
    fprintf(stdout,"I have received %d in process %d\n",c,rank);
    // fflush(stdout);

    c=factorial(c);
    MPI_Gather(&c,1,MPI_INT,B,1,MPI_INT,0,MPI_COMM_WORLD);
    if(rank==0)
    {
        fprintf(stdout,"The Result gathered in the root \n");
        for(i=0; i<N; i++)
        {
            fprintf(stdout,"%d \t",B[i]);
            sum+=B[i];
        }
        fprintf(stdout,"\nSum of all values: %d\n",sum);
    }
    fflush(stdout);
    MPI_Finalize();
    return 0;
}
// student@dbl-34:~/Documents/220962446_PCAP/Lab3$ mpirun -n 5 ./out1
// Enter 5 values:
// 1 2 3 4 5
// I have received 1 in process 0
// I have received 2 in process 1
// I have received 3 in process 2
// I have received 4 in process 3
// I have received 5 in process 4
// The Result gathered in the root 
// 1 	2 	6 	24 	120 	
// Sum of all values: 153
