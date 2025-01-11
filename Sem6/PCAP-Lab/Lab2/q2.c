/*2) Write a MPI program where the master process (process 0) sends a number to each of 
the slaves and the slave processes receive the number and prints it. Use standard send.*/
#include <mpi.h>
#include <stdio.h>

int main(int argc,char* argv[])
{
    int rank, size,x;
    MPI_Init(&argc,&argv);
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    MPI_Comm_size(MPI_COMM_WORLD,&size);
    MPI_Status status;
    if(rank==0)
    {
        int n;
        scanf("%d",&n);
        for(int i=1;i<size;i++)
        MPI_Send(&n,1,MPI_INT,i,1,MPI_COMM_WORLD);
        fflush(stdout);

    }
    else
    {
        MPI_Recv(&x,1,MPI_INT,0,1,MPI_COMM_WORLD,&status);
        fprintf(stdout,"Rank: %d, Number: %d\n",rank,x);

    }
    MPI_Finalize();
    return 0;
}
// student@dbl-34:~/Documents/220962446_PCAP/Lab2$ mpirun -n 5 ./outq2
// 12
// Rank: 1, Number: 12
// Rank: 2, Number: 12
// Rank: 3, Number: 12
// Rank: 4, Number: 12

