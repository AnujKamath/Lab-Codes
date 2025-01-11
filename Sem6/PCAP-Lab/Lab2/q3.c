//3) Write a MPI program to read N elements of the array in the root process (process 0) where N is equal to the total number of processes. The root process sends one value to each of the slaves. Let even ranked process finds square of the received element and odd ranked process finds cube of received element. Use Buffered send.
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
        printf("Enter %d values",size);
        int arr[size];
        for(int i=0;i<size;i++)
            scanf("%d",&arr[i]);

        for(int i=1;i<size;i++)
            MPI_Send(&arr[i],1,MPI_INT,i,1,MPI_COMM_WORLD);

        for(int i=1;i<size;i++)
            MPI_Recv(&arr[i],1,MPI_INT,i,1,MPI_COMM_WORLD,&status);

        printf("The Final Array values are:\n");
        for(int i=0;i<size;i++)
            printf("%d ",arr[i]);
        printf("\n");

    }
    else
    {
        MPI_Recv(&x,1,MPI_INT,0,1,MPI_COMM_WORLD,&status);
        if(rank%2)
        {
            x=x*x*x;
            MPI_Send(&x,1,MPI_INT,0,1,MPI_COMM_WORLD);
        }
        else
        {
            x=x*x;
            MPI_Send(&x,1,MPI_INT,0,1,MPI_COMM_WORLD);
        }
    }
    MPI_Finalize();
    return 0;
}
// student@dbl-34:~/Documents/220962446_PCAP/Lab2$ mpirun -n 5 ./out
// Enter 5 values1 2 3 4 5
// The Final Array values are:
// 1 8 9 64 25 

