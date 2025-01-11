/*4) Write a MPI program to read an integer value in the root process. 
Root process sends this value to Process1, Process1 sends this value to Process2 and so on. 
Last process sends the value back to root process. When sending the value each process will first increment the received value by one. 
Write the program using point to point communication routines.*/
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
        printf("Enter a number");
        scanf("%d",&n);

        MPI_Ssend(&n,1,MPI_INT,1,1,MPI_COMM_WORLD);

        MPI_Recv(&x,1,MPI_INT,size-1,1,MPI_COMM_WORLD,&status);

        fprintf(stdout,"Rank: %d, Number: %d\n",rank,x);
        fflush(stdout);


    }
    else
    {
        MPI_Recv(&x,1,MPI_INT,rank-1,1,MPI_COMM_WORLD,&status);
        fprintf(stdout,"Rank: %d, Number: %d \n",rank,x);
        if(rank<size-1)
        MPI_Ssend(&x,1,MPI_INT,rank+1,1,MPI_COMM_WORLD);
        else
        MPI_Ssend(&x,1,MPI_INT,0,1,MPI_COMM_WORLD);
        
    }
    MPI_Finalize();
    return 0;
}
// student@dbl-34:~/Documents/220962446_PCAP/Lab2$ mpirun -n 5 ./out
// Enter a number55
// Rank: 1, Number: 55 
// Rank: 2, Number: 55 
// Rank: 3, Number: 55 
// Rank: 4, Number: 55 
// Rank: 0, Number: 55
